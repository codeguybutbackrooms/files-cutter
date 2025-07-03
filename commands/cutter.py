import os
import subprocess
from core.utils import generate_new_filename, check_disk_space, is_supported_file
from core.error import print_error
from core.ffmpeg import build_ffmpeg_command
import shutil

def check_ffmpeg():
    if not shutil.which("ffmpeg"):
        print_error("ERR_105", "ffmpeg not found. Please install it or add it to PATH.")

def cut_media(input_file, start_time, end_time, force_new_file=False):
    if not os.path.isfile(input_file):
        print_error("ERR_100", f"File not found: {input_file}")

    if not is_supported_file(input_file):
        print_error("ERR_106", "Unsupported file format. Only .mp4, .mp3, .wav are supported.")

    check_ffmpeg()
    check_disk_space(input_file)

    # Output file naming
    output_file = generate_new_filename(input_file) if force_new_file else os.path.splitext(input_file)[0] + "_cut" + os.path.splitext(input_file)[1]

    print(f"▶️ Cutting file: {input_file}")
    print(f"🕒 From {start_time} to {end_time}")
    print(f"💾 Output: {output_file}")

    command = build_ffmpeg_command(input_file, start_time, end_time, output_file)

    try:
        subprocess.run(command, check=True)
        print("✅ Done!")
    except subprocess.CalledProcessError:
        print_error("ERR_102", "There's something occurred, try again.")
