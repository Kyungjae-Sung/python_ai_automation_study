# with open("08_naver_news.py", "r") as f:
#     content = f.read()
# print(content)

with open("test.txt", "w") as f:
    f.write("파이썬이 만들었어요")

with open("test.txt", "r") as f:
    content = f.read()
print(content)

with open("test.txt", "w") as f:
    f.write("파이썬이 다시 썼어요")

with open("test.txt", "r") as f:
    content = f.read()
print(content)

with open("test.txt", "a") as f:
    f.write("\n이건 클로드 씨가 가르쳐줘서 파이썬이 뒤이어 썼어요")

with open("test.txt", "r") as f:
    content = f.read()
print(content)