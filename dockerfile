# 使用官方 Python 运行时作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录的所有文件到容器中
COPY . .

# 安装依赖
RUN pip install --no-cache-dir flask requests

# 设置容器启动时监听的端口
EXPOSE 33333

# 启动 Flask 应用
CMD ["python", "main.py"]
