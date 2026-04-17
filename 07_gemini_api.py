from google import genai
import os
from dotenv import load_dotenv

# .env 파일에서 API Key 불러오기
load_dotenv()

# Gemini 클라이언트 설정
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

# Gemini에게 메시지 보내기
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="안녕하세요! 파이썬으로 처음 Gemini API를 호출해봤어요. 한 줄로 축하 메시지 보내주세요!"
)

# 응답 출력
print(response.text)