import argparse
import sys
from commands.cutter import cut_media
from core.error import print_error

def main():
    parser = argparse.ArgumentParser(
        description="🪓 files-cutter — Cut media files using ffmpeg",
        epilog="Example:\n  python main.py --start-from 0:30 --end-at 1:00 --nf file:video.mp4",
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('--start-from', type=str, required=True, help="Start time (e.g., 10, 0:30, 00:01:15)")
    parser.add_argument('--end-at', type=str, required=True, help="End time (e.g., 1:00, 02:00)")
    parser.add_argument('--nf', action='store_true', help="Force new output filename (avoid overwrite)")
    parser.add_argument('--cus-out-name', type=str, help="Custom output filename (e.g., myclip.mp4)")
    parser.add_argument('--version', action='store_true', help="Show version info")
    parser.add_argument('--help-extra', action='store_true', help="Show detailed help about time formats")

    parser.add_argument('file', type=str, help="Media file to cut, must begin with 'file:'")

    args = parser.parse_args()

    # Handle version
    if args.version:
        print("files-cutter v1.0.0")
        sys.exit(0)

    # Help for time formats
    if args.help_extra:
        print("""
⏱ Time Format Help:

Valid formats:
  10           = 10 seconds
  0:10         = 10 seconds
  0:0:10       = 10 seconds
  00:01:30     = 1 minute 30 seconds
  1:2:3.5      = 1 hour 2 minutes 3.5 seconds
""")
        sys.exit(0)

    # File validation
    if not args.file.startswith("file:"):
        print_error("ERR_104", "Missing 'file:' prefix. Example: file:myclip.mp4")
    input_file = args.file[5:]

    cut_media(
        input_file=input_file,
        start_time=args.start_from,
        end_time=args.end_at,
        force_new_file=args.nf,
        custom_name=args.cus_out_name
    )

if __name__ == "__main__":
    main()
