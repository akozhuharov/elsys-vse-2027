"""Вгражда записаните стъпки в visualizer.html.

Употреба:
    python3 tools/trace.py && python3 tools/build_visualizer.py
"""

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = ROOT / "tools" / "visualizer.template.html"
DATA = ROOT / "tools" / "trace-data.json"
OUT = ROOT / "visualizer.html"

START, END = "/*__DATA__*/", "/*__END__*/"


def main():
    html = TEMPLATE.read_text(encoding="utf-8")
    data = DATA.read_text(encoding="utf-8")
    if START not in html or END not in html:
        sys.exit("Липсва маркер за данните в шаблона")
    head, rest = html.split(START, 1)
    _, tail = rest.split(END, 1)
    OUT.write_text(head + START + data + END + tail, encoding="utf-8")
    print(f"{OUT.name}: {len(OUT.read_text(encoding='utf-8')) // 1024} KB")


if __name__ == "__main__":
    main()
