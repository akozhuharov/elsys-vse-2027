"""Записва изпълнението на всяка примерна програма ред по ред.

Пуска всеки файл от examples/ с sys.settrace и запазва за всяка стъпка:
реда, стека от функции, стойностите на променливите, изхода до момента и
файловете в папката. Резултатът се вгражда във visualizer.html.

Употреба:  python3 tools/trace.py
"""

import io
import json
import os
import pathlib
import shutil
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
EXAMPLES = ROOT / "examples"
MAX_STEPS = 400
MAX_REPR = 160

LESSONS = {
    "01-introduction": ("Въведение", "introduction.md"),
    "02-lists-and-for-loop": ("Списъци и for цикъл", "lists-and-for-loop.md"),
    "03-while-loop-and-dictionary": ("While цикъл и Dictionary", "while-loop-and-dictionary.md"),
    "04-file-handling": ("Работа с файлове", "file-handling.md"),
    "05-functions": ("Функции", "functions.md"),
    "06-import": ("Библиотеки/модули", "import.md"),
    "07-classes": ("Класове", "classes.md"),
}

SKIP_TYPES = (type(sys), type(lambda: 0), type)


def fmt(value, depth=0):
    """Четим за ученик вид на стойност - без адреси в паметта."""
    if isinstance(value, (bool, int, float, type(None))):
        return repr(value)
    if isinstance(value, str):
        return repr(value) if len(value) <= MAX_REPR else repr(value[:MAX_REPR] + "…")
    if depth > 2:
        return "…"
    if isinstance(value, list):
        return "[" + ", ".join(fmt(v, depth + 1) for v in value[:20]) + "]"
    if isinstance(value, tuple):
        inner = ", ".join(fmt(v, depth + 1) for v in value[:20])
        return "(" + inner + ("," if len(value) == 1 else "") + ")"
    if isinstance(value, dict):
        return "{" + ", ".join(
            f"{fmt(k, depth + 1)}: {fmt(v, depth + 1)}" for k, v in list(value.items())[:20]
        ) + "}"
    if isinstance(value, set):
        return "{" + ", ".join(fmt(v, depth + 1) for v in list(value)[:20]) + "}"
    if isinstance(value, range):
        return str(value)
    if hasattr(value, "__dict__") and not isinstance(value, SKIP_TYPES):
        attrs = ", ".join(f"{k}={fmt(v, depth + 1)}" for k, v in vars(value).items())
        return f"{type(value).__name__}({attrs})"
    text = str(value)
    return text if len(text) <= MAX_REPR else text[:MAX_REPR] + "…"


def type_name(value):
    return type(value).__name__


def snapshot(frame):
    """Променливите на един frame, без модули/функции/класове."""
    out = []
    for name, value in frame.f_locals.items():
        if name.startswith("__"):
            continue
        if isinstance(value, SKIP_TYPES):
            continue
        out.append({"name": name, "value": fmt(value), "type": type_name(value)})
    return out


def files_snapshot(sandbox):
    files = {}
    for entry in sorted(os.listdir(sandbox)):
        path = os.path.join(sandbox, entry)
        if not os.path.isfile(path):
            continue
        try:
            with open(path, "r", encoding="utf-8") as f:
                files[entry] = f.read()[:600]
        except (UnicodeDecodeError, OSError):
            files[entry] = "<двоичен файл>"
    return files


def trace_file(path):
    source = path.read_text(encoding="utf-8")
    lines = source.splitlines()
    first = lines[0].lstrip("# ").strip() if lines and lines[0].startswith("#") else path.stem
    title, _, description = first.partition(" - ")

    sandbox = os.path.join(tempfile.mkdtemp(prefix="elsys-"), "programa")
    os.makedirs(sandbox)
    steps = []
    stdout = io.StringIO()
    filename = str(path)
    code = compile(source, filename, "exec")
    globals_dict = {"__name__": "__main__", "__file__": filename, "__builtins__": __builtins__}

    def record(frame, event, arg):
        if len(steps) >= MAX_STEPS:
            return
        stack = []
        f = frame
        while f is not None and f.f_code.co_filename == filename:
            stack.append({
                "func": "<програма>" if f.f_code.co_name == "<module>" else f.f_code.co_name,
                "line": f.f_lineno,
                "vars": snapshot(f),
            })
            f = f.f_back
        stack.reverse()
        steps.append({
            "line": frame.f_lineno,
            "event": event,
            "stack": stack,
            "returned": fmt(arg) if event == "return" else None,
            "stdout": stdout.getvalue(),
            "files": files_snapshot(sandbox),
        })

    def local_tracer(frame, event, arg):
        if event in ("line", "return"):
            record(frame, event, arg)
        return local_tracer

    def global_tracer(frame, event, arg):
        if frame.f_code.co_filename != filename:
            return None
        if event == "call":
            return local_tracer
        return None

    cwd = os.getcwd()
    real_stdout = sys.stdout
    os.chdir(sandbox)
    sys.stdout = stdout
    error = None
    try:
        sys.settrace(global_tracer)
        exec(code, globals_dict)
    except Exception as exc:  # noqa: BLE001 - показваме грешката в страницата
        error = f"{type(exc).__name__}: {exc}"
    finally:
        sys.settrace(None)
        sys.stdout = real_stdout
        os.chdir(cwd)

    final_files = files_snapshot(sandbox)
    shutil.rmtree(os.path.dirname(sandbox), ignore_errors=True)

    # последна стъпка: краят на програмата
    steps.append({
        "line": None,
        "event": "end",
        "stack": [],
        "returned": None,
        "stdout": stdout.getvalue(),
        "files": final_files,
    })

    lesson_dir = path.parent.name
    lesson_title, lesson_md = LESSONS[lesson_dir]
    return {
        "id": f"{lesson_dir}/{path.name}",
        "lesson": lesson_title,
        "lessonDir": lesson_dir,
        "lessonMd": lesson_md,
        "file": f"examples/{lesson_dir}/{path.name}",
        "title": title,
        "description": description,
        "code": lines,
        "steps": steps,
        "output": stdout.getvalue(),
        "error": error,
    }


def main():
    programs = []
    for lesson_dir in sorted(LESSONS):
        for path in sorted((EXAMPLES / lesson_dir).glob("*.py")):
            data = trace_file(path)
            flag = f"ГРЕШКА {data['error']}" if data["error"] else "ok"
            print(f"{data['file']}: {len(data['steps'])} стъпки - {flag}", file=sys.stderr)
            programs.append(data)

    payload = json.dumps(programs, ensure_ascii=False, separators=(",", ":"))
    out = ROOT / "tools" / "trace-data.json"
    out.write_text(payload, encoding="utf-8")
    print(f"\n{len(programs)} програми -> {out} ({len(payload) // 1024} KB)", file=sys.stderr)


if __name__ == "__main__":
    main()
