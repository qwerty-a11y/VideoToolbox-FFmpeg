
# 🎬 视频处理工具箱 (Video Toolbox)

基于 Gradio 的 WebUI 视频处理工具，支持 GPU/CPU 字幕烧录、视频转码、批量处理、格式转换等功能。  
提供 **Python 源码版** 和 **Windows 独立 EXE 版**（无需安装 Python）。

---

##  主要功能

-  **GPU/CPU 字幕烧录**：自动匹配同名字幕（ASS/SRT），支持 GPU 加速
-  **GPU/CPU 视频转码**：递归处理子目录，保持原有目录结构
-  **批量上传文件**：拖拽或点击添加多个视频，自动查找同名字幕
-  **通用视频转换**：自定义输出格式、编码器、质量、位深（8bit / 10bit / 自动）
-  **10bit 视频智能处理**：若显卡不支持 10bit 编码，自动转为 8bit 并保持 GPU 加速
-  **WebUI 界面**：自动打开浏览器，支持 Windows / Linux
-  **实时日志输出**：显示转码进度和 FFmpeg 详细错误信息

---

## 📦 版本说明

| 版本 | 适用系统 | 运行方式 | 下载 |
|------|----------|----------|------|
| **源码版** | Windows / Linux | 需要 Python 3.8+ | 克隆本仓库 |
| **EXE 版** | Windows 10/11 | 双击运行，无需 Python | 从 [Releases](../../releases) 下载 `VideoToolbox.exe` |

---

## 🔧 源码版使用方法

### 1. 环境准备

- 安装 **Python 3.8+**（[官网下载](https://python.org)）
- 安装 **FFmpeg**（见下方 [FFmpeg 获取与配置](#ffmpeg-获取与配置)）

### 2. 克隆仓库

```bash
git clone https://github.com/pachothun18/VideoToolbox-FFmpeg.git
cd VideoToolbox-FFmpeg
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

`requirements.txt` 内容如下：
```
gradio==6.17.3
huggingface_hub==1.19.0
groovy==0.1.2
safehttpx==0.1.7
hf-gradio==0.4.1
gradio-client==2.5.0
```

### 4. 运行

- **Windows**：双击 `启动WebUI.bat`
- **Linux**：在终端执行 `bash 启动WebUI.sh`

首次运行时会自动检查并安装依赖，浏览器将自动打开 `http://localhost:7860`。

---

## ️ EXE 版使用方法

1. 从 [Releases](../../releases) 下载 `VideoToolbox.exe`
2. 下载 **FFmpeg** 可执行文件（见下方说明），将 `ffmpeg.exe` 和 `ffprobe.exe` 与 `VideoToolbox.exe` 放在**同一文件夹**
3. 双击 `VideoToolbox.exe` 运行，浏览器自动打开

> **注意**：EXE 版本不需要 Python 环境，但必须自行提供 FFmpeg。

---

##  FFmpeg 获取与配置

本工具依赖 FFmpeg 实现所有音视频处理。请根据您的系统下载对应版本：

### Windows 用户

推荐从以下两个站点下载：

- [gyan.dev](https://www.gyan.dev/ffmpeg/builds/) – 提供完整版（默认 GPL 许可证）
- [BtbN](https://github.com/BtbN/FFmpeg-Builds/releases) – 同时提供 **GPL** 和 **LGPL** 版本

> 下载后解压，将 `bin` 文件夹内的 `ffmpeg.exe` 和 `ffprobe.exe` 复制到与主程序（`video_toolbox.py` 或 `VideoToolbox.exe`）相同的目录下，或添加到系统 PATH 环境变量。

---

##  许可证

本项目使用 [MIT License](LICENSE)。  
**FFmpeg 是其各自所有者的项目，遵循 LGPL/GPL 许可证，与本项目独立。**

---

## 使用的开源项目

本项目便携版压缩包中内置了FFmpeg，在此展示所用版本及源码和许可证链接

FFmpeg (LGPL variant, autobuild-2026-06-11-14-22)
- 许可证：LGPLv3
- 源代码：https://github.com/FFmpeg/FFmpeg/archive/d30dead35e7fecae51ccd4602273153c87b1bbd9.zip
- 许可证原文：https://github.com/FFmpeg/FFmpeg/blob/master/COPYING.LGPLv3

项目所使用的Python库
| 名称              | 版本号     | 许可证                              |
|-------------------|-------------|--------------------------------------|
| Jinja2            | 3.1.6       | BSD License                          |
| MarkupSafe        | 3.0.3       | BSD-3-Clause                         |
| PyYAML            | 6.0.3       | MIT License                          |
| Pygments          | 2.20.0      | BSD-2-Clause                         |
| annotated-doc     | 0.0.4       | MIT                                  |
| annotated-types   | 0.7.0       | MIT License                          |
| anyio             | 4.13.0      | MIT                                  |
| brotli            | 1.2.0       | MIT                                  |
| certifi           | 2026.5.20   | Mozilla Public License 2.0 (MPL 2.0) |
| click             | 8.4.1       | BSD-3-Clause                         |
| colorama          | 0.4.6       | BSD License                          |
| exceptiongroup    | 1.3.1       | MIT License                          |
| fastapi           | 0.136.3     | MIT                                  |
| filelock          | 3.29.3      | MIT                                  |
| fsspec            | 2026.4.0    | BSD-3-Clause                         |
| gradio            | 6.17.3      | Apache-2.0                           |
| gradio_client     | 2.5.0       | Apache-2.0                           |
| groovy            | 0.1.2       | MIT License                          |
| h11               | 0.16.0      | MIT License                          |
| hf-gradio         | 0.4.1       | MIT                                  |
| hf-xet            | 1.5.1       | Apache-2.0                           |
| httpcore          | 1.0.9       | BSD-3-Clause                         |
| httpx             | 0.28.1      | BSD License                          |
| huggingface_hub   | 1.19.0      | Apache Software License              |
| idna              | 3.18        | BSD-3-Clause                         |
| markdown-it-py    | 4.2.0       | MIT License                          |
| mdurl             | 0.1.2       | MIT License                          |
| numpy             | 2.2.6       | BSD License                          |
| orjson            | 3.11.9      | MPL-2.0 AND (Apache-2.0 OR MIT)      |
| packaging         | 26.2        | Apache-2.0 OR BSD-2-Clause           |
| pandas            | 2.3.3       | BSD License                          |
| pillow            | 12.2.0      | MIT-CMU                              |
| pydantic          | 2.13.4      | MIT                                  |
| pydantic_core     | 2.46.4      | MIT                                  |
| pydub             | 0.25.1      | MIT License                          |
| python-dateutil   | 2.9.0.post0 | Apache Software License; BSD License |
| python-multipart  | 0.0.32      | Apache-2.0                           |
| pytz              | 2026.2      | MIT License                          |
| rich              | 15.0.0      | MIT License                          |
| safehttpx         | 0.1.7       | MIT License                          |
| semantic-version  | 2.10.0      | BSD License                          |
| shellingham       | 1.5.4       | ISC License (ISCL)                   |
| six               | 1.17.0      | MIT License                          |
| starlette         | 1.3.0       | BSD-3-Clause                         |
| tomlkit           | 0.14.0      | MIT License                          |
| tqdm              | 4.68.2      | MPL-2.0 AND MIT                      |
| typer             | 0.25.1      | MIT                                  |
| typing-inspection | 0.4.2       | MIT                                  |
| typing_extensions | 4.15.0      | PSF-2.0                              |
| tzdata            | 2026.2      | Apache-2.0                           |
| uvicorn           | 0.49.0      | BSD-3-Clause                         |