## 1단계: import 기본 설정
import requests # -> Naver API 호출
import json     # -> json 파일로 결과를 저장
import os       # -> 환경변수(API Key) 읽기
from dotenv import load_dotenv  # -> .env 파일 로드

load_dotenv()

## 2단계: 네이버 뉴스 검색 함수
def search_naver_news(query):
    url = "https://openapi.naver.com/v1/search/news.json"
    headers = {
        "X-Naver-Client-Id": os.environ.get("NAVER_CLIENT_ID"),
        "X-Naver-Client-Secret": os.environ.get("NAVER_CLIENT_SECRET")
    }
    params = {
        "query": query,
        "display": 3,
        "sort": "date"
    }
    response = requests.get(url,headers=headers, params=params)
    return response.json()

## 3단계: json 파일로 저장하는 함수
def save_news_to_file(news_data, filename):     # news_date -> 저장할 뉴스 데이터(딕셔너리)
    with open(filename, "w", encoding="utf-8") as f:    # filename -> 저장할 파일 이름(파라미터로 받음)
        json.dump(news_data, f, ensure_ascii=False, indent=2) # json.dump -> 딕셔너리를 json 파일로 저장
    print(f"{filename} 저장 완료!")


## 4단계: 실행 코드
    # 1. 뉴스 검색

news_data = search_naver_news("AI 기술")

    # 2. json 파일로 저장

save_news_to_file(news_data, "ai_news.json")

    # 3. 저장된 파일 읽어서 출력

with open("ai_news.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(f"총 {len(loaded['items'])}개의 뉴스를 가져왔어요!")
for i, item in enumerate(loaded["items"]):
    print(f"[{i+1}] {item['title']}")