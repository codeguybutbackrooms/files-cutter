import os
import subprocess
import shutil

from core.utils import (
    generate_new_filename,
    check_disk_space,
    is_supported_file,
    get_media_duration,
    parse_time_to_seconds
)
from core.error import print_error
from core.ffmpeg import build_ffmpeg_command
from core import SUPPORTED_FORMATS

def check_ffmpeg():
    """
    Ensure ffmpeg and ffprobe are available in PATH.
    """
    if not shutil.which("ffmpeg"):
        print_error("ERR_105", "❌ ffmpeg not found. Please install it or add it to your system PATH.")
    if not shutil.which("ffprobe"):
        print_error("ERR_105", "❌ ffprobe not found. Please install ffmpeg (which includes ffprobe).")

def cut_media(input_file, start_time, end_time, force_new_file=False, custom_name=None):
    """
    Main cutting function. Handles all checks and runs ffmpeg to cut the file.
    """

    # ERR_103: File not found
    if not os.path.isfile(input_file):
        print_error("ERR_103", f"File not found: {input_file}")

    # ERR_104: Unsupported format
    if not is_supported_file(input_file):
        print_error("ERR_104", f"Unsupported file format. Supported: {', '.join(SUPPORTED_FORMATS)}")

    # ERR_105: ffmpeg/ffprobe missing
    check_ffmpeg()

    # ERR_101: Not enough disk space
    if not check_disk_space(input_file):
        print_error("ERR_101", "You don't have enough space for it.")

    # ERR_110: Could not retrieve duration (handled inside get_media_duration if needed)
    duration = get_media_duration(input_file)
    if duration is None:
        print_error("ERR_110", "Could not determine media duration.")

    print(f"📏 Media duration: {duration:.2f} seconds")

    try:
        start_sec = parse_time_to_seconds(start_time)
        end_sec = parse_time_to_seconds(end_time)
    except:
        print_error("ERR_105", "Invalid time format. Use mm:ss or hh:mm:ss.")

    # ERR_107: Start time > duration
    if start_sec >= duration:
        print_error("ERR_107", "The specified start time is longer than the media file.")

    # ERR_108: End time > duration
    if end_sec > duration:
        print_error("ERR_108", "The specified end time is longer than the media file.")

    # ERR_103 (reused): Start >= end
    if start_sec >= end_sec:
        print_error("ERR_103", "Start time must be earlier than end time.")

    # ERR_111: --cus-out-name is used but empty
    if custom_name is not None and custom_name.strip() == "":
        print_error("ERR_111", "Custom output name (--cus-out-name) is missing or empty.")

    # Determine output file name
    if custom_name:
        output_file = custom_name
    else:
        output_file = (
            generate_new_filename(input_file)
            if force_new_file
            else os.path.splitext(input_file)[0] + "_cut" + os.path.splitext(input_file)[1]
        )

    # ERR_106: Output file already exists
    if os.path.exists(output_file) and not force_new_file and not custom_name:
        print_error("ERR_106", f"Output file already exists: {output_file}")

    print(f"▶️ Cutting file: {input_file}")
    print(f"🕒 From: {start_time} → {end_time}")
    print(f"💾 Output file: {output_file}")

    command = build_ffmpeg_command(input_file, start_time, end_time, output_file)

    try:
        subprocess.run(command, check=True)
        print("✅ Cutting complete!")
    except subprocess.CalledProcessError:
        print_error("ERR_102", "Something went wrong while cutting. Please try again.")
