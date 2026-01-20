import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

# 核心参数实验
completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "system", "content": "你是一个营养学家。"},
        {"role": "user", "content": "人为什么要吃饭"}
    ],
    temperature=0.1,    # 控制随机性：0.1 接近确定性，1.0 非常发散
    max_tokens=500,     # 限制生成长度，防止浪费 Token 额度
    top_p=0.8           # 核采样：控制模型只在概率最高的 80% 词汇中选择
)

print(completion.choices[0].message.content)