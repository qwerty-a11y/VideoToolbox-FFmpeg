#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
视频处理工具箱 - Gradio WebUI 入口
"""

import os
import socket
import sys
import threading
import warnings
import webbrowser

# 嵌入式Python环境默认不会将脚本自身路径加入 sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 抑制 Starlette 弃用警告（Gradio 内部依赖）
warnings.filterwarnings("ignore", category=DeprecationWarning, module="starlette")
warnings.filterwarnings("ignore", message=".*HTTP_422_UNPROCESSABLE_ENTITY.*")

from app.ui.app import create_ui


def main():
    demo = create_ui()
    demo.queue()

    port = 7860
    max_port = 7900
    found_port = None
    while port <= max_port:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('localhost', port))
            found_port = port
            break
        except OSError:
            port += 1
    if found_port is None:
        print("无法找到可用端口，将使用默认 7860（可能冲突）")
        found_port = 7860

    threading.Timer(2, lambda: webbrowser.open(f"http://localhost:{found_port}")).start()
    demo.launch(server_name="localhost", server_port=found_port, share=False)


if __name__ == "__main__":
    main()
