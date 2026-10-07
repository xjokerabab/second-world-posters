"""根据 data/*.txt 生成 gallery/*.md 图片墙。只展示 images/ 下已下载的图片。"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COLS = 3

SECTIONS = {
    "official": [
        ("@Sukiea1008（Su）原帖示例", "https://x.com/Sukiea1008/status/2107363303920140592", slice(None)),
    ],
    "featured": [("高赞精选", None, slice(None))],
    "community": [("社区作品", None, slice(None))],
}
TITLES = {"official": "官方示例", "featured": "高赞精选", "community": "社区作品"}


def grid(category, ids):
    ids = [i for i in ids if (ROOT / "images" / category / f"{i}.jpg").exists()]
    if not ids:
        return "_图片尚未下载，见 README「图片下载」。_\n"
    rows = []
    for start in range(0, len(ids), COLS):
        cells = [
            f'<td width="33%"><a href="../images/{category}/{i}.jpg">'
            f'<img src="../images/{category}/{i}.jpg" width="100%"></a></td>'
            for i in ids[start:start + COLS]
        ]
        rows.append("<tr>" + "".join(cells) + "</tr>")
    return "<table>\n" + "\n".join(rows) + "\n</table>\n"


for category, parts in SECTIONS.items():
    ids = (ROOT / "data" / f"{category}.txt").read_text().split()
    out = [f"# {TITLES[category]}\n", "[← 返回首页](../README.md)\n"]
    for heading, link, sl in parts:
        sub = ids[sl]
        out.append(f"## {heading}（{len(sub)} 张）\n")
        if link:
            out.append(f"原帖：<{link}>\n")
        out.append(grid(category, sub))
    out.append("\n> 图片版权归各自作者所有，本仓库仅作收集展示。\n")
    (ROOT / "gallery" / f"{category}.md").write_text("\n".join(out))
    print(f"gallery/{category}.md")
