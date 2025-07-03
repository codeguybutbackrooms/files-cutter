import os
import shutil
from core import SUPPORTED_FORMATS
from core.error import print_error

def generate_new_filename(base_path):
    """
    Generate a new output filename to avoid overwriting.
    Examples: file_cut.mp4, file_cut_1.mp4, file_cut_2.mp4...
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
