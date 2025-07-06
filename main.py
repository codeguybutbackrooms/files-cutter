import argparse
from commands.cutter import cut_media
from core.error import print_error

VERSION = "1.0.1"

def main():
    parser = argparse.ArgumentParser(
        description="🪓 files-cutter — Cut media files using ffmpeg",
        epilog="Syntax:\n  python main.py --start-from 0:10 --end-at 1:00 file:video.mp4"
    )

    parser.add_argument("--start-from", required=True, help="Start time (hh:mm:ss or mm:ss)")
    parser.add_argument("--end-at", required=True, help="End time (hh:mm:ss or mm:ss)")
    parser.add_argument("--nf", action="store_true", help="Create a new file (don't overwrite)")
    parser.add_argument("--cus-out-name", help="Custom output filename (auto applies --nf)")
    parser.add_argument("--version", action="store_true", help="Show program version")
    parser.add_argument("--help-extra", action="store_true", help="Show advanced usage/help")
    parser.add_argument("file", nargs="?", help="Media input (format: file:yourfile.mp4)")

    args = parser.parse_args()

    # Show version
    if args.version:
        print(f"files-cutter version {VERSION}")
        return

    # Extra help
    if args.help_extra:
        print("""
🔧 Extra Help:
  --nf              Save as a new file with a unique name
  --cus-out-name    Name the output file manually (auto uses --nf)
  file:filename     Must prefix the input with 'file:' (e.g., file:video.mp4)

Examples:
  python main.py --start-from 0:10 --end-at 0:30 file:video.mp4
  python main.py --start-from 1:00 --end-at 2:00 --cus-out-name cut.mp4 file:myvideo.mp4
        """)
        return

    # Validate input file
    if not args.file or not args.file.startswith("file:"):
        print_error("ERR_109", "Missing input. Use format: file:yourfile.mp4")

    input_file = args.file[5:].strip()

    if args.cus_out_name is not None and args.cus_out_name.strip() == "":
        print_error("ERR_111", "--cus-out-name is missing or empty.")

    # Auto force new file if custom name is used
    force_new_file = args.nf or bool(args.cus_out_name)

    # Main call
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
    except Exception as e:
        print_error("ERR_102", f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()
