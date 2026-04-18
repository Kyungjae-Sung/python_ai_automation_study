# with open("08_naver_news.py", "r") as f:
#     content = f.read()
# print(content)

# # 1. txt 파일 io
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


# ## 2. json 파일 io
# import json

# # 뉴스 데이터 딕셔너리
# news = {
#     "title": "AI 반도체 수출 역대 최고",
#     "date": "2026-04-18",
#     "category": "AI"
# }

# # json 파일로 저장
# with open("news.json", "w", encoding="utf-8") as f:
#     json.dump(news, f, ensure_ascii=False, indent=2)
# print("저장 완료!")

# # json 파일로 읽기
# with open("news.json", "r", encoding="utf-8") as f:
#     loaded = json.load(f)
# print(loaded)
# print(loaded["title"])


# # 3. os모듀로로 파일 io
# import os

# # 현재 폴더의 파일 목록 보기
# files = os.listdir(".")
# print(files)

# # 파일 / 폴더 구분하기
# for file in files:
#     if os.path.isfile(file):
#         print(f"파일: {file}")


# 4. 여러 파일 한번에 읽기
# .py 파일만 골라서 읽기
import os
files = os.listdir(".")
for file in files:
    if file.endswith(".py"):
        print(f"=== {file} ===")

# 내 웹사이트 글 폴더에서 txt 파일만 골라서 읽기
for file in files:
    if file.endswith(".txt"):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
        print(f"=== {file} ===")
        print(content)
