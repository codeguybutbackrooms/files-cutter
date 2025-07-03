def build_ffmpeg_command(input_file, start, end, output_file):
    return [
        "ffmpeg",
        "-i", input_file,
        "-ss", start,
        "-to", end,
        "-c", "copy",
        output_file
    ]
