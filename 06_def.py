def say_hello():
    print("Hello")
    print("Nice to meet you")

say_hello()


name = "kj"
name1 = "claude"

def say_hello(person):
    print(f"hello, {person} nice to mee you")

say_hello(name)
say_hello(name1)
say_hello("kyungjae")

# 정리
# 파라미터는 함수를 유연하게 만들어주는 빈칸입니다. 빈 칸에 뭘 넣느냐에 따라 함수가 다르게 동작합니다. 파라미터가 없으면 함수는 항상 같은 일만하고, 파라미터가 있으면 하나의 함수로 수백가지 상황을 처리할 수 있습니다.

def make_prompt():
    print("파이썬에 대해 설명해줘")

make_prompt() #-> 몇번을 해도 같은 내용만 출력

# 다른 주제를 만들고 싶다면, 함수를 새로 만들어야 합니다.

def make_prompt_python():
    print("파이썬을 설명해줘")

def make_prompt_langchain():
    print("langchain에 대해 설명해줘")

def make_prompt_rag():
    print("RAG에 대해 설명해줘")

# 필요한 함수를 항상 만들어야 해서 비효율적입니다.

def make_prompt(topic):
    print(f"{topic}에 대해 설명해줘")

make_prompt("파이썬") # -> 파이썬을 설명해줘
make_prompt("Langchain") # -> langchain에 대해 설명해줘
make_prompt("RAG") # -> RAG에 대해 설명해줘

# 함수는 하나인데 {topic} 에 뭘 넣느냐에 따라 결과가 달라집니다. {topic}이 파라미터 입니다.

# 파라미터를 여러 개 쓸 수도 있습니다.

def make_prompt(topic, language, length):
    print(f"{topic}에 대해 {language}로 {length}줄 이내로 설명해줘")

make_prompt("파이썬", "한국어", 3) # -> 파이썬에 대해 한국어로 3줄 이내로 설명해줘
make_prompt("RAG", "영어", 5) # -> RAG에 대해 영어로 5줄 이내로 설명해줘


## return: 결과값을 돌려주기

# print와 return의 차이
# print -> 스피커(소리를 밖으로 내보내기만하고, 저장하지 못함)
# return -> 택배(값을 포장해서 돌려줌, 받아서 활용가능)

def add_print(a,b):
    print(a + b)
result = add_print(3,5)
print(result)

def add_return(a,b):
    return a + b
result = add_return(3, 7)
print(result)
print(f"3 + 7 = {result}")

# return의 실용성
def make_prompt(topic, language):
    return f"{topic}에 대해 {language}로 설명해줘"

# return으로 만들면 이렇게 활용 가능
prompt = make_prompt("python", "한국어")
print(prompt)
print(f"AI에게 보낼 메시지: {prompt}")



## "define make_prompt, which takes topic and language as temporary variables (parameters) to work with"

# 1. make_prompt("파이썬", "한국어") 호출
# 2. topic = "파이썬", language = "한국어" 로 채워짐
# 3. f"{topic}에 대해 {language}로 설명해줘" 완성
# 4. return으로 그 결과물을 돌려줌
# 5. prompt 변수가 그 결과물을 받아서 담음


# 다만 파라미터 안의 topic, language는 일반 변수와 살짝 달라요. 함수 밖에서 쓰는 변수(name = "kj")는 어디서든 쓸 수 있지만, 파라미터는 함수 안에서만 쓸 수 있는 임시 변수예요.

# def make_prompt(topic, language):
#     return f"{topic}에 대해 {language}로 설명해줘"
#     # topic, language는 여기 안에서만 존재

# print(topic)  # ❌ 에러! 함수 밖에서는 topic을 모름