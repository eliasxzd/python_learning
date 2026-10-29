# 读取api_key，创建客户端
from openai import OpenAI
import sys

# 获取api_key
def load_api_key(path="api_key.txt"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            api_key = f.read().strip()
            if not api_key:
                print("API文件为空")
                sys.exit(1)
            return api_key
    except FileNotFoundError:
        print("API文件没有找到:"+path)
        sys.exit(1)

# 创建客户端
def create_client(api_key):
    return OpenAI(api_key=api_key,base_url="https://open.bigmodel.cn/api/paas/v4",timeout=30)

if __name__ == "__main__":
    api_key = load_api_key("api_key.txt")
    client = create_client(api_key)
    if not (api_key and client):
        print("客户端创建失败")
        sys.exit(1)
    else:
        print("客户端创建成功")