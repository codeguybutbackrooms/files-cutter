import argparse
import sys
from commands.cutter import cut_media
from core.error import print_error

VERSION = "1.0.2"

def main():
    parser = argparse.ArgumentParser(
        description="🪓 files-cutter — Cut media files using ffmpeg",
        epilog="""
## Syntax:
  files-cutter --start-from <start> --end-at <end> file:<file>

Examples:
  files-cutter --start-from 0:10 --end-at 1:00 file:video.mp4
  files-cutter --start-from 0:05 --end-at 2:30 --nf file:song.mp3
  files-cutter --start-from 0:00 --end-at 0:30 --cus-out-name intro_cut.mp4 file:long.mp4
"""
    )

    parser.add_argument("--start-from", required=True, help="Start time (hh:mm:ss or mm:ss)")
    parser.add_argument("--end-at", required=True, help="End time (must be later than start)")
    parser.add_argument("--nf", action="store_true", help="Save as a new file (don’t overwrite)")
    parser.add_argument("--cus-out-name", help="Custom output file name (auto applies --nf)")
    parser.add_argument("--version", action="store_true", help="Show version")
    parser.add_argument("--help-extra", action="store_true", help="Show extended help")
    parser.add_argument("file", nargs="?", help="Target file. Format: file:yourfile.mp4")

    args = parser.parse_args()

    # Show version
    if args.version:
        print(f"files-cutter version {VERSION}")
        sys.exit(0)

    # Show extra help
    if args.help_extra:
        print("""
🪓 files-cutter — cut .mp4/.mp3/.webm/.ogg/.wav using ffmpeg

Required:
  --start-from        Start time (e.g., 0:10 or 00:00:10)
  --end-at            End time (must be later than start)
  file:<file>         Input file path (e.g., file:video.mp4)

Optional:
  --nf                Force new output file to avoid overwriting
  --cus-out-name      Custom output filename (automatically enables --nf)
  --version           Show tool version
  --help-extra        Show this extended help

🕒 Time Format:
  You can use either:
    - mm:ss (e.g., 1:30 means 1 minute 30 seconds)
    - hh:mm:ss (e.g., 0:01:30 also means 1 minute 30 seconds)

  ✅ Supported:
    1:10      → 1 min 10 sec
    0:45      → 45 sec
    00:02:00  → 2 min
    1:00:00   → 1 hour

Examples:
  files-cutter --start-from 0:10 --end-at 1:00 file:clip.mp4
  files-cutter --start-from 1:00 --end-at 2:00 --nf file:song.mp3
  files-cutter --start-from 0:00 --end-at 0:30 --cus-out-name preview.mp4 file:full_video.mp4
""")
        sys.exit(0)

    # Validate file argument
    if not args.file or not args.file.lower().startswith("file:"):
        print_error("ERR_109", "Missing or invalid input file. Use format: file:filename.mp4")

    input_file = args.file[5:].strip()

    # Empty custom name check
    if args.cus_out_name is not None and args.cus_out_name.strip() == "":
        print_error("ERR_111", "--cus-out-name is missing or empty.")

    # Auto apply --nf if custom name used
    force_new_file = args.nf or bool(args.cus_out_name)

    try:
        cut_media(
            input_file=input_file,
            start_time=args.start_from,
            end_time=args.end_at,
            force_new_file=force_new_file,
            custom_name=args.cus_out_name
        )
    except KeyboardInterrupt:
        print("\n⛔ Operation cancelled.")
        sys.exit(1)
    except Exception as e:
        print_error("ERR_102", f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
