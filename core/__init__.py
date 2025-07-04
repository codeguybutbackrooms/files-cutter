__version__ = "1.0.1"

# Supported file extensions for media cutting
from core import SUPPORTED_FORMATS

# Re-export core functions correctly from core/
from core.utils import generate_new_filename, check_disk_space, is_supported_file
from core.error import print_error
from core.ffmpeg import build_ffmpeg_command
