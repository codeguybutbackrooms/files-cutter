from commands.cutter import cut_media
from core.error import print_error
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="🪓 files-cutter — trim media files (mp4/mp3/wav...)")
    parser.add_argument("--start-from", required=True, help="Start time (e.g., 0:10, 00:01:30)")
    parser.add_argument("--end-at", required=True, help="End time (e.g., 9:10, 00:09:10)")
    parser.add_argument("--nf", action="store_true", help="Force new output file (avoid overwrite)")
    parser.add_argument("file", help="File to cut. Prefix with 'file:' (e.g., file:video.mp4)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()

    if not args.file.startswith("file:"):
        print_error("ERR_104", "File must be prefixed with 'file:', like: file:video.mp4")

    filename = args.file[5:]
    cut_media(filename, args.start_from, args.end_at, force_new_file=args.nf)
