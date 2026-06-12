#!/bin/bash
# 视频工具箱 Linux 启动脚本（自动管理虚拟环境）

cd "$(dirname "$0")"

# 虚拟环境目录名
VENV_DIR="venv"

# 1. 检查 python3 命令是否存在（仅用于创建虚拟环境）
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到 python3，请安装 Python 3.8+"
    exit 1
fi

# 2. 如果虚拟环境不存在，则自动创建
if [ ! -d "$VENV_DIR" ]; then
    echo "未找到虚拟环境 $VENV_DIR，正在创建..."
    python3 -m venv "$VENV_DIR"
    if [ $? -ne 0 ]; then
        echo "错误: 创建虚拟环境失败"
        exit 1
    fi
    echo "虚拟环境创建成功"
fi

# 3. 激活虚拟环境
source "$VENV_DIR/bin/activate"

# 4. 安装/更新依赖（使用虚拟环境中的 pip）
if [ -f "requirements.txt" ]; then
    echo "正在检查/安装 requirements.txt 中的依赖..."
    pip install -r requirements.txt --quiet
else
    echo "未找到 requirements.txt，尝试安装 gradio..."
    python -c "import gradio" &> /dev/null
    if [ $? -ne 0 ]; then
        pip install gradio --quiet
    fi
fi

# 5. 检查 ffmpeg（可选）
if ! command -v ffmpeg &> /dev/null; then
    echo "警告: 未找到 ffmpeg，请安装 ffmpeg 以确保转码功能正常"
fi

# 6. 后台启动服务
echo "启动视频工具箱..."
python video_toolbox.py &
PID=$!

echo "工具箱已启动，PID=$PID。浏览器将自动打开。关闭此终端不会停止服务。"