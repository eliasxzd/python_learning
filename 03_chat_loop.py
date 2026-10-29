from utils import load_api_key, create_client
from openai import OpenAI, AuthenticationError, APIConnectionError, RateLimitError 
import sys

api_key = load_api_key("api_key.txt")
client = create_client(api_key)

messages = [{"role": "system", "content": "你是一个中文助手"}]

while True:
    user_input = input("用户: ")
    if user_input == "exit":
        print("退出程序")
        break
    if user_input == "clear":
        messages = [{"role": "system", "content": "你是一个中文助手"}]
        print("对话已经清空")
        continue
    messages.append({"role": "user", "content": user_input})
    
    try:
        stream = client.chat.completions.create(
            model="glm-4-flash",
            messages=messages,
            stream=True,
        )
        print("GLM:",end=" ")
        full_reply= " "
        for reply in stream:
            chiok = reply.choices[0].delta.content
            if chiok != None:
                print(chiok,end="", flush=True)
                full_reply += chiok
        messages.append({"role": "assistant", "content": full_reply})
        print("\n")

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
