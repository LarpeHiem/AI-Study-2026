import os
from openai import OpenAI

# 1. 模拟“检索”步骤：手动读取本地文件
with open("knowledge.txt", "r", encoding="utf-8") as f:
    local_knowledge = f.read()

# 2. 初始化客户端
client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 3. 增强生成：把本地知识喂给 Prompt
prompt = f"""
你是一个极其负责的转码导师。
请参考以下背景知识来回答我的问题。如果知识里没写，就说不知道。

背景知识：
{local_knowledge}

问题：我 2026 年的目标是什么？
"""

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[{"role": "user", "content": prompt}],
    temperature=0 # 设为 0，确保严谨，不乱编
)

print(completion.choices[0].message.content)