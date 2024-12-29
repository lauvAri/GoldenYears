# 夕颜乐龄

本项目为面向老年人的AI手机操作系统，此代码仓库为项目后端代码。

本团队研发的产品精准定位于 60 岁及以上的老年人群体。这一群体在面对智能手机日益复杂的操作时往往存在诸多困难，我们的 AI 手机操作助手旨在为他们提供便捷、易懂的手机操作引导服务，助力其跨越数字鸿沟，畅享科技带来的便利与乐趣。

## 功能介绍

用户在客户端输入请求，服务端程序接收请求后，借助UI理解框架，帮助用户自动操作手机，降低了用户操作手机的复杂度，提高了操作效率。

## 环境部署

### 前置要求

1. Python 3.8
2. Android SDK

### 运行项目

```
git clone 
conda create -n visiontasker python=3.8
pip install -r requirements.txt
uvicorn main:app --reload
```

### 项目配置

`core/LLM_api.py` 修改使用的LLM的key和id

`element/detect_text/text_detection.py` 修改OCR模型的key和id

## 文件说明

`main.py` 项目的启动文件，创建websocket程序，与前端进行通讯

`server.py` 项目的后端运算文件，接受用户的请求，并帮助用户操作手机

## 输入设备

请参考使用[ADBKeyBoard](https://github.com/senzhk/ADBKeyBoard)

## 模型

[☁️ Google Drive](https://drive.google.com/drive/folders/1ij5Y5JhUb8cPTAr8fZ0jfyenoNUqr5nP?usp=sharing)

[☁️ Quark Cloud Drive](https://pan.quark.cn/s/f2f707e26a08)

## 致谢

本项目实现基于西安交通大学智能网络与网络安全教育部重点实验室提出的[基于视觉的移动设备任务自动化方案](https://arxiv.org/abs/2312.11190)，没有他们的贡献，本项目不会如此完善。在此，致以诚挚的谢意。
