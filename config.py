import os
from dotenv import load_dotenv, dotenv_values

# 自动搜索 .env 文件
load_dotenv(verbose=True)
# 读取.env中的配置
APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
