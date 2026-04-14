## 1. 변수 만들기 (상자에 데이터 담기)
name = 'kyungjae'
age = 40
today_task = 'Project Learning_Python'

## 2. 옛날 방식 (더하기 사용 - 불편하고 에러가 잘 납니다)
## 숫자인 age를 문자로 바꾸기 위해 str()을 써야 하는 번거로움이 있습니다.
print("환영합니다. " + name + "님! 나이는 " + str(age) + " 이시군요.")

## 3. 요즘방식 : f-string
## 문자열 앞에 알파벳 'f'를 붙이고, 변수를 중괄호{} 안에 넣기만 하면 됩니다.
print(f"환영합니다. {name}님! 나이는 {age} 이시군요.")
print(f"오늘의 목표는 [{today_task}] 이네요. 파이팅!")

## 4. f-string의 강력한 기능 (중괄호 안에서 계산도 가능)
print(f"{name}님은 8월 이면 {age +1}이 되시네요")