"""Записва секцията "Примерни програми" във всеки .md файл от курса.

Източник на истината са .py файловете в examples/ и реално записаният изход
от tools/trace.py - затова в учебника никога не стои изход, който програмата
не дава. Секцията между маркерите се презаписва при всяко пускане.

Употреба:  python3 tools/trace.py && python3 tools/sync_examples.py
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = json.loads((ROOT / "tools" / "trace-data.json").read_text(encoding="utf-8"))

START = "<!-- ПРИМЕРИ:НАЧАЛО (генерирано от tools/sync_examples.py - не редактирай ръчно) -->"
END = "<!-- ПРИМЕРИ:КРАЙ -->"

NOTE = {
    "04-file-handling": (
        "> [!IMPORTANT]\n"
        "> Трите програми създават файловете си в папката, от която ги пускаш.\n"
    ),
}


def section(programs, lesson_dir):
    parts = [
        START,
        "",
        "## Примерни програми",
        "",
        f"Кодът е в [`examples/{lesson_dir}/`](./examples/{lesson_dir}/) — пусни го с "
        f"`python3 examples/{lesson_dir}/<име>.py`.",
        "Виж го ред по ред, с променливите и изхода на всяка стъпка, във "
        "[визуализатора](./visualizer.html).",
        "",
    ]
    if lesson_dir in NOTE:
        parts += [NOTE[lesson_dir], ""]

    for i, prog in enumerate(programs, 1):
        code = "\n".join(prog["code"])
        output = prog["output"].rstrip("\n")
        parts += [
            f"### {i}. {prog['title']}",
            f"*{prog['description']}*" if prog["description"] else "",
            "",
            "```python",
            code,
            "```",
            "",
            "Изход:",
            "```",
            output,
            "```",
            "",
        ]
    parts += [END, ""]
    return "\n".join(line for line in parts if line is not None)


def main():
    by_lesson = {}
    for prog in DATA:
        by_lesson.setdefault(prog["lessonDir"], []).append(prog)

    for lesson_dir, programs in by_lesson.items():
        md_path = ROOT / programs[0]["lessonMd"]
        text = md_path.read_text(encoding="utf-8")
        new = section(programs, lesson_dir)

        if START in text and END in text:
            head = text.split(START)[0]
            tail = text.split(END, 1)[1]
            text = head + new + tail.lstrip("\n")
        else:
            text = text.rstrip("\n") + "\n\n" + new

        md_path.write_text(text, encoding="utf-8")
        print(f"{md_path.name}: {len(programs)} примера")


if __name__ == "__main__":
    main()
