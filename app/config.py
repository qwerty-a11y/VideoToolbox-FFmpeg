import os
import shutil
import sys
from pathlib import Path


def get_base_dir():
    if getattr(sys, 'frozen', False):
        return Path(sys.executable).parent
    else:
        return Path(__file__).parent.parent


BASE_DIR = get_base_dir()

FFMPEG_PATH = shutil.which("ffmpeg")
FFPROBE_PATH = shutil.which("ffprobe")

local_ffmpeg = BASE_DIR / "ffmpeg.exe"
local_ffprobe = BASE_DIR / "ffprobe.exe"
if local_ffmpeg.exists():
    FFMPEG_PATH = str(local_ffmpeg)
if local_ffprobe.exists():
    FFPROBE_PATH = str(local_ffprobe)

if not FFMPEG_PATH:
    FFMPEG_PATH = "ffmpeg"
if not FFPROBE_PATH:
    FFPROBE_PATH = "ffprobe"

IGNORE_DIRS = {'output', 'fonts', 'python', '__pycache__', '.git', '.venv', 'app'}
VIDEO_EXTENSIONS = {'.mp4', '.mkv', '.avi', '.mov', '.flv', '.wmv', '.m4v', '.rmvb'}
SUBTITLE_EXTENSIONS = {'.ass', '.srt'}
PREFERRED_LANG = 'SC'
