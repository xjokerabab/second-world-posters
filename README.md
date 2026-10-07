# 第二世界 Second World · AI 海报作品集

[English](README.en.md)

「第二世界」是一种 AI 海报风格：**上半部分忠实保留真实照片，下半部分在暖色纸面上用剪纸、照片碎片和极简黑色手绘线条，把照片里的场景延续下去**。道路、水面、光线或身体动作从照片里穿过中缝，进入一个物理规则不同的「第二世界」。

本仓库收集这一风格的提示词与社区作品，共 **97 张**（已去重）。

## 原作者 Credits

| 角色 | 作者 | 原帖 |
|---|---|---|
| 原始英文提示词 | **Su** [@Sukiea1008](https://x.com/Sukiea1008) | <https://x.com/Sukiea1008/status/2107363303920140592> |
| 中文结构化版本 | **虎小象** [@hx831126](https://x.com/hx831126) | <https://x.com/hx831126/status/2107414034538496398> |

提示词版权归原作者所有。社区作品版权归各自创作者所有，本仓库仅作收集与展示，不用于商业用途。如原作者或图片作者希望修改署名或移除内容，请[提交 Issue](../../issues)，我们会尽快处理。

## 提示词

- [原版英文提示词](prompts/original-english.md)（作者 [@Sukiea1008](https://x.com/Sukiea1008)）
- 中文版请前往 [@hx831126 原帖](https://x.com/hx831126/status/2107414034538496398) 获取

使用方法见 [docs/how-to-use.md](docs/how-to-use.md)。

## 作品集

| 分类 | 数量 | 说明 |
|---|---|---|
| [官方示例](gallery/official.md) | 8 | @Sukiea1008 与 @hx831126 原帖示例图 |
| [高赞精选](gallery/featured.md) | 15 | 社区高赞作品 |
| [社区作品](gallery/community.md) | 74 | 原帖回复、引用及传播中的作品 |

## 仓库结构

```
├── prompts/              提示词
├── data/                 各分类的图片 ID 列表（一行一个）
├── images/               下载的原图，按分类存放
├── gallery/              图片墙页面（脚本生成）
├── scripts/
│   ├── download_images.sh  按 data/ 下载图片
│   └── build_gallery.py    生成 gallery/ 页面
└── docs/how-to-use.md
```

## 图片下载

图片由 GitHub Actions 自动下载：修改 `data/*.txt` 并推送到 `main` 后，[Download images](.github/workflows/download-images.yml) 工作流会下载新图片、重建图片墙并提交。也可以在 Actions 页面手动运行，或在本地执行：

```bash
./scripts/download_images.sh
python3 scripts/build_gallery.py
```

## 贡献

欢迎提交你用「第二世界」提示词生成的作品，见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可

仓库自身的文字说明与脚本以 [CC0 1.0](LICENSE) 发布。**提示词与图片不在此许可范围内**，版权归各自作者所有。
