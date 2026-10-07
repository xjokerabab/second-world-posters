# 使用方法

提示词：[prompts/original-english.md](../prompts/original-english.md)（作者 [@Sukiea1008](https://x.com/Sukiea1008)）

## 基本步骤

1. 准备一张照片。画面中最好有一条能自然延伸到画面中部的结构：道路、海岸线、水面、倒影、树枝、光线、建筑线条或人物动作。
2. 在支持「图片 + 文字」输入的工具中上传照片，粘贴完整提示词。
3. 每次只上传一张照片，提示词要求一张照片生成一张独立海报。
4. 输出比例设为竖版 **3:4**。

## 各工具提示

| 工具 | 建议 |
|---|---|
| ChatGPT / GPT-Image | 直接上传照片并粘贴提示词，效果最接近原作 |
| Gemini | 同上，上传照片后粘贴提示词 |
| 即梦 / 豆包 | 使用图生图，粘贴提示词，比例选 3:4 |
| Midjourney | 用 `--cref` 或图片链接作参考，加 `--ar 3:4`；对「上半部分保持原图」的遵循度较弱 |
| Flux（Kontext 等） | 用图像编辑模式，比例选 3:4 |

## 小技巧

- 照片里的延伸结构越清晰，上下衔接越自然。
- 结果里上半部分照片被改动了，可以补一句 "Keep the upper half exactly as the original photo."
- 手写英文标注想换成中文，可以把 Caption 一节改成 "Add one short handwritten Chinese caption"。
