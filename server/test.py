import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("UPSTAGE_API_KEY")

from openai import OpenAI



print(API_KEY)

client = OpenAI(
    api_key=API_KEY, 
    base_url="https://api.upstage.ai/v1/solar"
)

chat_result = client.chat.completions.create(
    model="solar-pro",
    messages=[
        {"role": "system", "content": "모든 답변은 존댓말로 답변해줘."},
        {"role": "user", "content": "한국의 수도는 어디야?"},
    ],
)

print(chat_result.choices[0].message.content)