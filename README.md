# 🪓 files-cutter

A lightweight CLI tool to cut audio/video files (MP4, MP3, WAV, OGG, WEBM...) using `ffmpeg`.  
Inspired by `yt-dlp`, built for clean offline media slicing — no pip install required.

---

## ✨ Features

- ✅ Cut media between start and end times
- ✅ Supports: `.mp4`, `.mp3`, `.wav`, `.ogg`, `.webm`
- ✅ Keeps original quality (no re-encoding)
- ✅ Clear error codes (`ERR_101`, `ERR_107`, etc.)
- ✅ No Python dependencies — uses only standard library

---

## 🧾 Syntax

```bash
python main.py --start-from [START_TIME] --end-at [END_TIME] [OPTIONS] file:[FILENAME]
```
`--start-from`: Specifies the time to begin cutting the file.
`--end-at`: Specifies the time to stop cutting the file.
`file`: Specifies which file

## ⏱ Accepted Time Formats
| Format      | Interpreted As     | Notes                                                                 |
| ----------- | ------------------ | --------------------------------------------------------------------- |
| `10`        | 10 seconds         | Pure seconds (no colon)                                               |
| `0:10`      | 0 min 10 sec       | `minutes:seconds` format                                              |
| `0:0:10`    | 0 hr 0 min 10 sec  | `hours:minutes:seconds`, works with leading zeroes                    |
| `00:00:10`  | 0 hr 0 min 10 sec  | Same as above, more readable                                          |
| `01:30`     | 1 min 30 sec       | Useful for short clips                                                |
| `1:02:03.5` | 1 hr 2 min 3.5 sec | Accurate to half-seconds or milliseconds if needed (`.5`, `.25`, etc) |
| `02:00:00`  | Exactly 2 hours    | Long format, great for movies or recordings                           |
