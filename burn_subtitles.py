import os
import sys

# 嵌入式Python环境默认不会将脚本自身路径加入 sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from app.core.filesystem import find_all_video_subtitle_pairs
from app.commands.profiles import LIBX264
from app.pipeline.job import run_job

OUTPUT_DIR = os.path.join(BASE_DIR, "output")


def main():
    os.chdir(BASE_DIR)
    print("=== 动漫字幕烧录工具 (CPU稳定版) ===")
    print(f"工作目录: {BASE_DIR}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pairs = find_all_video_subtitle_pairs(BASE_DIR)
    if not pairs:
        print("未找到匹配的视频和字幕文件对。")
        sys.exit(1)

    print(f"找到 {len(pairs)} 个文件对，开始处理...\n")
    success = 0
    for video, sub, rel_dir in pairs:
        print(f"视频: {os.path.relpath(video, BASE_DIR)}")
        print(f"字幕: {os.path.relpath(sub, BASE_DIR)}")

        out_subdir = os.path.join(OUTPUT_DIR, rel_dir)
        os.makedirs(out_subdir, exist_ok=True)
        name_without_ext = os.path.splitext(os.path.basename(video))[0]
        output_path = os.path.join(out_subdir, f"{name_without_ext}_hardsub.mp4")

        if os.path.exists(output_path):
            print(f"  跳过: {output_path}")
            success += 1
            print()
            continue

        print(f"  CPU处理中: {os.path.basename(video)}")
        ok, logs = run_job(video, output_path, LIBX264, quality=23, audio_codec='aac', audio_bitrate='128k', sub_path=sub)
        for log in logs:
            print(f"  {log}")
        if ok:
            success += 1
        print()

    print(f"=== 完成，成功: {success}/{len(pairs)} ===")


if __name__ == "__main__":
    main()
