# Second World · AI Poster Collection

[中文](README.md)

"Second World" is an AI poster style: **the upper half keeps a real photo faithfully, and the lower half continues the same scene on warm ivory paper** with cut-paper shapes, photo fragments and minimal black hand-drawn lines. A road, shoreline, ray of light or body movement crosses the center seam into a world with different physical rules.

This repository collects the prompt and **93** artworks (deduplicated).

## Credits

| Role | Author | Source |
|---|---|---|
| Prompt author | **Su** [@Sukiea1008](https://x.com/Sukiea1008) | <https://x.com/Sukiea1008/status/2107363303920140592> |

The prompt belongs to its original author, and every artwork belongs to its creator. This repository only collects and showcases them, for non-commercial purposes. If you are an author and want a credit changed or content removed, please [open an issue](../../issues).

## Prompt

[Original English prompt](prompts/original-english.md) by [@Sukiea1008](https://x.com/Sukiea1008)

See [docs/how-to-use.md](docs/how-to-use.md) for usage.

## Gallery

| Category | Count | Notes |
|---|---|---|
| [Official examples](gallery/official.md) | 4 | Examples from @Sukiea1008's post |
| [Featured](gallery/featured.md) | 15 | Popular community works |
| [Community](gallery/community.md) | 74 | Replies, quotes and reposts |

## Images

Images are downloaded by GitHub Actions. Push a change to `data/*.txt` on `main` and the [Download images](.github/workflows/download-images.yml) workflow fetches new images, rebuilds the gallery and commits. You can also run it manually from the Actions tab, or locally:

```bash
./scripts/download_images.sh
python3 scripts/build_gallery.py
```

## License

The repository's own text and scripts are released under [CC0 1.0](LICENSE). **The prompt and images are not covered** and remain the property of their respective authors.
