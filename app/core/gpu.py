import subprocess


def get_nvidia_gpu_info():
    try:
        result = subprocess.run(
            ['nvidia-smi', '--query-gpu=name,driver_version', '--format=csv,noheader'],
            capture_output=True, text=True, encoding='utf-8', errors='ignore'
        )
        if result.returncode == 0:
            parts = result.stdout.strip().split(',')
            if len(parts) >= 2:
                return parts[0].strip(), parts[1].strip()
    except Exception:
        pass
    return None, None
