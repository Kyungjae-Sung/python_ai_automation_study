import requests
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# 네이버 뉴스 검색 함수
def search_naver_news(query):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": os.environ.get("NAVER_CLIENT_ID"),
        "X-Naver-Client-Secret": os.environ.get("NAVER_CLIENT_SECRET")
    }
    params = {
        "query": query,
        "display": 1,
        "sort": "date"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# 글 생성 함수
def generate_article(news_title, news_description):
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    prompt = f"""
다음 AI 뉴스를 바탕으로 기술 블로그 글을 작성해주세요.

뉴스 제목: {news_title}
뉴스 내용: {news_description}

작성 조건:
- 독자: AI 기술에 관심 있는 일반인
- 분량: 800~1200자
- 형식: 한 줄 요약 → 본문(뉴스 요약 + 기술 설명) → 마무리(전망)
- 언어: 한국어
- 원문기사 링크:
"""
    response = client.models.generate_content(
        model="gemini-3-pro-preview",
        contents=prompt
    )
    return response.text

# 실행
news_data = search_naver_news("AI 기술")
item = news_data["items"][0]

print("=== 원본 뉴스===")
print(f"제목: {item['title']}")
print(f"내용: {item['description']}")
print()
print("=== AI 생성 기술 블로그 글===")
article = generate_article(item['title'], item['description'])
print(article)

