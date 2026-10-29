# 读取api_key，连接大模型，发送请求，并接收回复，打印（一次性）
from openai import OpenAI
import sys
from openai import OpenAI, AuthenticationError, APIConnectionError, RateLimitError

# 读取api_key
try:
    with open("api_key.txt","r",encoding="utf-8") as f:
        api_key = f.read().strip()
    if not api_key:
        print("api_key为空") 
        sys.exit(1)
except FileNotFoundError:
    print("文件没有找到")
    sys.exit(1)
except Exception as e:
    print("读取错误：",e)
    sys.exit(1)

# 创建OpenAI客户端
client = OpenAI(api_key=api_key,base_url="https://open.bigmodel.cn/api/paas/v4")

# 发送请求
try:
    response = client.chat.completions.create(
        model="glm-4-flash",
        messages=[
            {"role": "user", "content": "你好，请介绍一下自己"}
        ],
    )
except APIConnectionError as e:
    print("连接错误：",e)
    sys.exit(1)
except AuthenticationError:
    print("认证错误")
    sys.exit(1)
except RateLimitError:
    print("请求频率过高")
    sys.exit(1)
except Exception as e:
    print("创建客户端失败：",e)
    sys.exit(1)
    
# 输出响应
print(response.choices[0].message.content)