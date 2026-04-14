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