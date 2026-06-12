"""视频处理工具箱 - Gradio WebUI."""
import gradio as gr

from app.core.ffmpeg import check_encoder_support
from app.core.gpu import get_nvidia_gpu_info
from app.ui import tab_subtitle, tab_transcode, tab_upload, tab_convert


def create_ui():
    with gr.Blocks() as demo:
        gr.Markdown("# 视频处理工具箱")
        gr.Markdown("支持GPU/CPU字幕烧录、GPU/CPU视频转码。递归处理子目录，保持原有结构。")

        with gr.Row():
            gpu_name, driver = get_nvidia_gpu_info()
            gpu_status = f"GPU: {gpu_name} (驱动 {driver})" if gpu_name else "未检测到NVIDIA GPU"
            enc_h264 = check_encoder_support('h264_nvenc')
            enc_hevc = check_encoder_support('hevc_nvenc')
            enc_status = f"h264_nvenc: {'OK' if enc_h264 else '--'} | hevc_nvenc: {'OK' if enc_hevc else '--'}"
            gr.Markdown(f"**系统状态**：{gpu_status} &nbsp;&nbsp; {enc_status}")

        with gr.Tabs():
            tab_subtitle.build()
            tab_transcode.build()
            tab_upload.build()
            tab_convert.build()

        gr.Markdown("""---
### 使用说明
- **递归处理**：自动扫描所有子文件夹，输出保持相同目录结构
- **字幕配对**：优先匹配同名的`.ass`/`.srt`，语言偏好`SC`（简体）
- **GPU要求**：10bit视频自动降级8bit（使用滤镜）避免编码失败；纯GPU转码需显卡支持对应编码器
- **FFmpeg**：请确保`ffmpeg.exe`（Windows）或`ffmpeg`（Linux）位于同目录或PATH中""")

    return demo
