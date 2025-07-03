# 🪓 files-cutter

A lightweight CLI tool to cut audio/video files (MP4, MP3, WAV, OGG, WEBM...) using `ffmpeg`.  
Inspired by `yt-dlp` — but for slicing media files quickly and offline.

---

## ✨ Features

- ✅ Cut media from start to end time
- ✅ Supports: `.mp4`, `.mp3`, `.wav`, `.ogg`, `.webm`
- ✅ Keeps original quality (no re-encode)
- ✅ Prevent overwrite with `--nf` (new file) flag
- ✅ Clean error codes (like `ERR_101`, `ERR_105`...)

---

## 🧾 Syntax

```bash
python main.py --start-from [START_TIME] --end-at [END_TIME] [OPTIONS] file:[FILENAME]
