user_age = 40
weather = "Rain"
print("=== 1. 나이 확인 (기본 if) ===")
## if 뒤에 조건(질문)을 쓰고, 끝에 꼭 콜론(:)을 붙입니다.
if user_age >= 20:
    ## 조건이 참(true)일 때 실행할 코드는 반드시 '들여쓰기(Tab)'를 해야 합니다
    print("성인입니다. 주류 구매가 가능합니다.")
else: # 아니면 (위 조건이 거짓이면)
    print("미성년자입니다. 주류 구매가 불가능합니다.")

print("\n=== 2. 날씨 확인 (조건이 여러 개일 때 - elif) ===")
if weather == "rain": # 파이썬에서 '같다'는 기호를 두번(==)쓴다
    print("오늘 비가 오네요. 우산을 꼭 챙기세요")
elif weather == "snow": # else if 의 줄임말 (아니고 만약 눈이 오면)
    print("눈이 오네요! 미끄러움 주의하세요.")
else: # 비도 아니고 눈도 아니면 (나머지 모든 경우)
    print("날씨가 맑거나 흐릅니다. 좋은 하루 보내세요.")


score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")


print(100 == 99) # -> False
print(100 == 100) # -> True

print(100 != 99) # -> Ture
print(100 != 100) # -> False

print(score > 90) # -> Flase
print(score < 90) # -> True

print(score >= 80) # -> True
print(score <= 80) # -> False


age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("입장가능")
else:
    print("입장불가")

response = "success"

if response == "success":
    print("다음 단계 진행")
elif response == "error":
    print("원인 파악하고 다시시도합니다")
else:
    print("알 수 없는 응답입니다")


temperature = 23

if temperature >= 28:
    print("더워서 에어컨가동")
elif temperature >19:
    print("온도가 적당합니다")
else:
    print("온도가 춥습니다")


user_grade = "admin"

if user_grade == "admin":
    print("관리자입니다")
elif user_grade == "user":
    print("사용자입니다")
else:
    print("알 수 없는 등급입니다")