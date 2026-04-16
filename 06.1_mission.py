## Lv.1 함수 만들기

def make_prompt(topic, language):
    return f"{topic}에 대해 {language}로 설명해주세요"
prompt = make_prompt("파이썬", "한국어")
print(prompt)


## Lv.2 파라미터 하나 더 추가하기

def make_prompt(topic, language, length):
    return f"{topic}에 대해 {language}로 {length}줄로 설명해주세요"
prompt = make_prompt("파이썬", "한국어", 5)
print(prompt)


## Lv.3 함수에 조건 추가하기

def check_length(length):
    if length <= 3:
        return f"{length}이하로 짧게 답변해주세요"
    elif length <= 7:
        return f"{length}이하로 보통으로 답변해주세요"
    else:
        return f"{length}이상으로 길게 답변 해주세요"
    

## Lv.4 두 함수를 조합하기

def make_prompt(topic, language, length):
    return f"{topic}에 대해 {language}로 {length}줄로 설명해주세요."
prompt = make_prompt("파이썬", "한국어", 8)
answer = check_length(8)
print("AI 요청 정보")
print(f"프롬프트: {prompt}")
print(f"답변유형: {answer}")