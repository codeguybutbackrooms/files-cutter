import os
import shutil
import subprocess
from core import SUPPORTED_FORMATS
from core.error import print_error

def generate_new_filename(base_path):
    """
    Generate a new output filename to avoid overwriting.
    Examples: file_cut.mp4, file_cut_1.mp4, etc.
    """
    name, ext = os.path.splitext(base_path)
    counter = 1
    new_path = f"{name}_cut{ext}"
    while os.path.exists(new_path):
        new_path = f"{name}_cut_{counter}{ext}"
        counter += 1
    return new_path

def check_disk_space(file_path):
    """
    Ensure at least 2x the file's size is free on disk.
    """
    try:
        total, used, free = shutil.disk_usage(os.path.dirname(file_path) or ".")
        input_size = os.path.getsize(file_path)
        if free < input_size * 2:
            print_error("ERR_101", "You don't have enough space for it.")
    except Exception:
        print_error("ERR_102", "Failed to check disk space.")

def is_supported_file(file_path):
    """
    Check whether the file extension is supported.
    """
    ext = os.path.splitext(file_path)[1].lower()
    return ext in SUPPORTED_FORMATS

def get_media_duration(file_path):
    """
    Use ffprobe to get the media duration in seconds.
    Requires ffprobe (bundled with ffmpeg).
    """
    try:
        result = subprocess.run(
            [
                "ffprobe", "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                file_path
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return float(result.stdout.strip())
    except Exception:
        return None

def parse_time_to_seconds(timestr):
    """
    Convert time string like '10', '0:10', or '0:0:10' to seconds.
    """
    try:
        parts = list(map(float, timestr.split(":")))
        if len(parts) == 1:
            return parts[0]
        elif len(parts) == 2:
            return parts[0] * 60 + parts[1]
        elif len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
        else:
            return 0
    except Exception:
        print_error("ERR_103", f"Invalid time format: {timestr}")
