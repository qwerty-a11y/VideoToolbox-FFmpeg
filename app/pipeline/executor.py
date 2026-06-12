import subprocess


def run_ffmpeg(cmd: list[str], cwd: str | None = None) -> tuple[bool, list[str]]:
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='ignore', cwd=cwd)
        if result.returncode == 0:
            return True, []
        else:
            errors = []
            if result.stderr:
                for line in result.stderr.strip().split('\n'):
                    errors.append(f"FFmpeg错误: {line}")
            if result.stdout:
                for line in result.stdout.strip().split('\n'):
                    errors.append(f"FFmpeg输出: {line}")
            return False, errors
    except Exception as e:
        return False, [f"异常: {str(e)}"]
