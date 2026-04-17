import anthropic
import os
from dotenv import load_dotenv

# .env 파일에서 API Key 불러오기
load_dotenv()

# Claude 클라이언트 생성
client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY")
)

# Claude에게 메시지 보내기
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "안녕하세요! 파이썬으로 처음 API를 호출해봤어요. 한 줄로 축하 메시지 보내주세요!"}
    ]
)

# 응답 출력
print(message.content[0].text)