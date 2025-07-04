__version__ = "1.0.1"

# Supported file extensions for media cutting
SUPPORTED_FORMATS = ['.mp4', '.mp3', '.wav', '.webm', '.ogg']

# Re-export core functions
from .error import print_error
from .ffmpeg import build_ffmpeg_command
