"""根据 data/*.txt 把作品图片墙写入 README.md 和 README.en.md 的标记区间。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLS = 3
SOURCE = "https://x.com/Sukiea1008/status/2107363303920140592"

SECTIONS = {
    "README.md": [
        ("official", "官方示例", f"来自 [@Sukiea1008]({SOURCE}) 原帖"),
        ("community", "社区作品", None),
    ],
    "README.en.md": [
        ("official", "Official Examples", f"From [@Sukiea1008]({SOURCE})'s post"),
        ("community", "Community", None),
    ],
}


def grid(category):
    ids = (ROOT / "data" / f"{category}.txt").read_text().split()
    ids = [i for i in ids if (ROOT / "images" / category / f"{i}.jpg").exists()]
    rows = []
    for start in range(0, len(ids), COLS):
        cells = [
            f'<td width="33%"><a href="images/{category}/{i}.jpg">'
            f'<img src="images/{category}/{i}.jpg" width="100%"></a></td>'
            for i in ids[start:start + COLS]
        ]
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return len(ids), "<table>\n" + "\n".join(rows) + "\n</table>"


for readme, sections in SECTIONS.items():
    parts = []
    for category, title, note in sections:
        count, table = grid(category)
        parts.append(f"### {title} · {count}\n")
        if note:
            parts.append(note + "\n")
        parts.append(table + "\n")
    path = ROOT / readme
    text = path.read_text()
    text = re.sub(
        r"(<!-- gallery:start -->).*?(<!-- gallery:end -->)",
        lambda m: m.group(1) + "\n" + "\n".join(parts) + m.group(2),
        text,
        flags=re.S,
    )
    path.write_text(text)
    print(readme)
