# with open("08_naver_news.py", "r") as f:
#     content = f.read()
# print(content)

## txt 파일 io
# with open("test.txt", "w") as f:
#     f.write("파이썬이 만들었어요")

# with open("test.txt", "r") as f:
#     content = f.read()
# print(content)

# with open("test.txt", "w") as f:
#     f.write("파이썬이 다시 썼어요")

# with open("test.txt", "r") as f:
#     content = f.read()
# print(content)

# with open("test.txt", "a") as f:
#     f.write("\n이건 클로드 씨가 가르쳐줘서 파이썬이 뒤이어 썼어요")

# with open("test.txt", "r") as f:
#     content = f.read()
# print(content)


## json 파일 io
import json

# 뉴스 데이터 딕셔너리
news = {
    "title": "AI 반도체 수출 역대 최고",
    "date": "2026-04-18",
    "category": "AI"
}

# json 파일로 저장
with open("news.json", "w", encoding="utf-8") as f:
    json.dump(news, f, ensure_ascii=False, indent=2)
print("저장 완료!")

# json 파일로 읽기
with open("news.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)
print(loaded)
print(loaded["title"])