## 1. list(리스트) : 데이터를 순서대로 담기
## 대괄호[] 를 사용한다.
topics = ["IT", "경제", "정치", "연예"]

print(f"내가 가장 좋아하는 주제 목록 : {topics}")
print(f"가장 첫 번째 주제 : {topics[0]}")
print(f"두 번째 주제 : {topics[1]}")
print(f"세 번째 주제 : {topics[2]}")
print(f"네 번째 주제 : {topics[3]}")
print("-" * 30)

## 2. Dictionary (딕셔너리) : 이름표(key)를 붙여서 데이터(value) 담기
## 중괄호 {} 를 사용한다.
user_info = {
    "name": "kyungjae",
    "age": 40,
    "job": "AI Automation Master",
    "interests": ["Python", "MySQL", "AI", "RAG", "Langchain"]
}

print(f"사용자 전체 정보: {user_info}")

## 딕셔너리에서 데이터를 꺼낼때는 이름표(key)를 부르면 됩니다.
print(f"사용자 이름: {user_info['name']}")
print(f"사용자 직업: {user_info['job']}")
print(f"첫번째 관심사: {user_info['interests'][2]}")

## 복습 
## 3. list
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["KJ", 40, True]

## 3.1 list에서 데이터 꺼내기
print(fruits[0])
print(fruits[1])
print(fruits[2])

## 3.2 list 수정하기
fruits[0] = "mango" # apple -> mango 교체
fruits.append("grape") # 맨뒤에 grape 추가
print(fruits)

# AI 자동화 연결 : 리스트는 "AI가 처리해야할 여러개의 항목" 을 담을때 사용한다. 분석할 뉴스 기사10, 번역할 문장 100개, 처리할 파일 이름 목록 등이 모두 리스트로 관리된다.

## 4. dictionary : 이름표가 붙은 데이터 보관함

person = {
    "name" : "KJ",
    "age" : 40,
    "job" : "automation developer"
}

print(person["name"])
print(person["age"])
print(person["job"])

person["age"] = 41
person["hobby"] = "coding"

print(person)

# AI 자동화 연결 : 딕셔너리는 AI API를 사용할 때 자주 씁니다. AI에게 요청을 보낼때와 AI의 응답을 받을 때 모두 딕셔너리 형태로 데이터가 오고 갑니다.

request = {
    "model" : "Opus",
    "prompt" : "explain python in 3lines",
    "language" : "Korean"
}