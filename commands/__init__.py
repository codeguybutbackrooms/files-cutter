# core/__init__.py

__version__ = "1.0.0"

# Supported file extensions for media cutting
SUPPORTED_FORMATS = ['.mp4', '.mp3', '.wav', '.webm', '.ogg']

# Re-export core functions
from .utils import generate_new_filename, check_disk_space, is_supported_file
from .error import print_error
from .ffmpeg import build_ffmpeg_command
