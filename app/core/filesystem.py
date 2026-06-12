import os
import random
import shutil
import string
import tempfile
from app.config import IGNORE_DIRS, VIDEO_EXTENSIONS, SUBTITLE_EXTENSIONS, PREFERRED_LANG


def random_str(k=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


def create_temp_work_dir():
    temp_base = tempfile.gettempdir()
    job_id = random_str(8)
    work_dir = os.path.join(temp_base, f'ffmpeg_job_{job_id}')
    os.makedirs(work_dir, exist_ok=True)
    return work_dir


def create_hardlink_or_copy(src, dst):
    try:
        os.link(src, dst)
        return 'link'
    except Exception:
        shutil.copy2(src, dst)
        return 'copy'


def find_all_video_subtitle_pairs(root_dir):
    pairs = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        videos, subs = [], []
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in VIDEO_EXTENSIONS:
                videos.append(f)
            elif ext in SUBTITLE_EXTENSIONS:
                subs.append(f)
        for v in videos:
            v_name = os.path.splitext(v)[0]
            candidates = [s for s in subs if s.lower().startswith(v_name.lower())]
            if not candidates:
                continue
            if PREFERRED_LANG:
                lang_candidates = [s for s in candidates if f'.{PREFERRED_LANG}-' in s or f'.{PREFERRED_LANG}.' in s]
                if lang_candidates:
                    candidates = lang_candidates
            chosen = next((s for s in candidates if s.lower().endswith('.ass')), candidates[0])
            video_path = os.path.join(dirpath, v)
            sub_path = os.path.join(dirpath, chosen)
            rel_dir = os.path.relpath(dirpath, root_dir)
            if rel_dir == '.':
                rel_dir = ''
            pairs.append((video_path, sub_path, rel_dir))
    return pairs


def find_all_videos(root_dir):
    videos = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in IGNORE_DIRS]
        for f in filenames:
            ext = os.path.splitext(f)[1].lower()
            if ext in VIDEO_EXTENSIONS:
                full_path = os.path.join(dirpath, f)
                rel_dir = os.path.relpath(dirpath, root_dir)
                if rel_dir == '.':
                    rel_dir = ''
                videos.append((full_path, rel_dir))
    return videos
