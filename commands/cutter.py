import os
import subprocess
import shutil

from core import (
    generate_new_filename,
    check_disk_space,
    is_supported_file,
    get_media_duration,
    parse_time_to_seconds,
    print_error,
    build_ffmpeg_command,
    SUPPORTED_FORMATS
)

def check_ffmpeg():
    """
    Ensure ffmpeg and ffprobe are available in PATH.
    """
    if not shutil.which("ffmpeg"):
        print_error("ERR_105", "ffmpeg not found. Please install it or add it to your system PATH.")
    if not shutil.which("ffprobe"):
        print_error("ERR_105", "ffprobe not found. Please install ffmpeg (which includes ffprobe).")

def cut_media(input_file, start_time, end_time, force_new_file=False, custom_name=None):
    """
    Main cutting function. Handles all checks and runs ffmpeg to cut the file.
    """
    if not os.path.isfile(input_file):
        print_error("ERR_100", f"File not found: {input_file}")

    if not is_supported_file(input_file):
        print_error("ERR_106", f"Unsupported file format. Supported: {', '.join(SUPPORTED_FORMATS)}")

    check_ffmpeg()
    check_disk_space(input_file)

    # Check media duration
    duration = get_media_duration(input_file)
    if duration is not None:
        print(f"📏 Media duration: {duration:.2f} seconds")

        start_sec = parse_time_to_seconds(start_time)
        end_sec = parse_time_to_seconds(end_time)

        if start_sec >= duration:
            print_error("ERR_107", "The specified start time is longer than the media file.")
        if end_sec > duration:
            print_error("ERR_108", "The specified end time is longer than the media file.")
        if start_sec >= end_sec:
            print_error("ERR_103", "Start time must be earlier than end time.")

    # Determine output file name
    if custom_name:
        output_file = custom_name
    else:
        output_file = (
            generate_new_filename(input_file)
            if force_new_file
            else os.path.splitext(input_file)[0] + "_cut" + os.path.splitext(input_file)[1]
        )

    print(f"▶️ Cutting file: {input_file}")
    print(f"🕒 From: {start_time} → {end_time}")
    print(f"💾 Output file: {output_file}")

    command = build_ffmpeg_command(input_file, start_time, end_time, output_file)

    try:
        subprocess.run(command, check=True)
        print("✅ Cutting complete!")
    except subprocess.CalledProcessError:
        print_error("ERR_102", "Something went wrong while cutting. Please try again.")
