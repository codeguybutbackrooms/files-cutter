# 🪓 files-cutter

A lightweight CLI tool to cut audio/video files (MP4, MP3, WAV, OGG, WEBM...) using `ffmpeg`.  
Inspired by `yt-dlp`, built for clean offline media slicing — no pip install required.

---

## [📁 Install it.](https://github.com/codeguybutbackrooms/files-cutter/releases/)
---
## 🛠️ How to Set Up
### 📦 Step-by-Step:
0. Doing everything in <a href="https://github.com/codeguybutbackrooms/files-cutter/edit/main/requirements.md">requirements.md</a> because it needs setup
1. Install the repo by the link
2. Right-click on the file, choose it, click "Extract Here", it will create a folder name: `files-cutter-main`
3. Click Windows, type "Command Prompt"
4. Copy this code to paste in ```cd %USERPROFILE%\Downloads\files-cutter-main``` and Enter

## ✨ Features

- ✅ Cut media between start and end times
- ✅ Supports: `.mp4`, `.mp3`, `.wav`, `.ogg`, `.webm`
- ✅ Keeps original quality (no re-encoding)
- ✅ Clear error codes (`ERR_101`, `ERR_107`, etc.)
- ✅ No Python dependencies — uses only standard library

---

## 🧾 Syntax

```bash
python main.py --start-from [MINUTES:SECONDS] --end-at [MINUTES:SECONDS] file:[NAME].example
```
*Make sure the "file:" and file name does not have space* <br>
`--start-from`: Specifies the time to begin cutting the file. <br>
`--end-at`: Specifies the time to stop cutting the file. <br>
`file`: Specifies which file <br>

## ✅ Optional
The following options enhance behavior but are not required: <br>
`--fps`: Sets the output video's frame rate (FPS) with syntax `--fps <value>`, the `<value>` is a integer (number), or default (Keeps the original video FPS, no change)
`--show-fps`: Show the maximum fps of the video
`--nf`: Stands for new file, forces the output to be saved as a new file to avoid overwriting the original. <br>
`--cus-out-name`: Stands for Custom Output Filename, this will change the output name to anything you want, and automatically behaves like --nf. <br>
`--version`: Show current version of files-cutter <br>
`--help`: Show main commands <br>
`--help-extra`: Show time formats <br>



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


## ❌ Error Codes Reference
| Error Code | Description                                                                           |
| ---------- | ------------------------------------------------------------------------------------- |
| `ERR_101`  | ❌ You don't have enough disk space to complete the cut/export.                        |
| `ERR_102`  | ❌ An unknown error occurred. Try running the command again.                           |
| `ERR_103`  | ❌ File not found. Please check the filename or path.                                  |
| `ERR_104`  | ❌ Unsupported file format. Supported formats: `.mp4`, `.mp3`, `.wav`, `.webm`, `.ogg` |
| `ERR_105`  | ❌ Invalid time format. Use `mm:ss` or `hh:mm:ss`.                                     |
| `ERR_106`  | ❌ Output file already exists. Use `--nf` or `--cus-out-name` to override.             |
| `ERR_107`  | ❌ The specified **start time is longer than the media duration**.                     |
| `ERR_108`  | ❌ The **end time is shorter than or equal to the start time**.                        |
| `ERR_109`  | ❌ No `file:` argument found. Specify a file using `file:filename.ext`                 |
| `ERR_110`  | ❌ MoviePy processing failed. Check file integrity or file permissions.                |
| `ERR_111`  | ❌ `--cus-out-name` was used but no name was provided.                                 |
