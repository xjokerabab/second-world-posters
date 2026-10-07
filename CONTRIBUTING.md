# 贡献指南

欢迎提交你用「第二世界」提示词生成的作品。

## 提交方式

**方式一：Issue**（最简单）
[新建 Issue](../../issues/new)，附上作品图片或推文链接，并写明作者名（X/微博等账号）。

**方式二：Pull Request**
1. 把图片放到 `images/community/`，文件名用英文或数字，格式 `.jpg` / `.png`。
2. 把文件名（不含扩展名）加到 `data/community.txt` 末尾。
3. 运行 `python3 scripts/build_gallery.py` 更新图片墙。
4. 在 PR 描述中写明作者与原始链接。

如果作品发在 X 上，也可以只把图片 ID（`pbs.twimg.com/media/<ID>.jpg` 中的 `<ID>`）加到 `data/community.txt`，合并后 GitHub Actions 会自动下载。

## 要求

- 只提交你本人创作，或已获作者同意的作品。
- 注明使用的工具（可选），方便其他人参考。
