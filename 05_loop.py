## 여러 개의 데이터가 담긴 바구니(리스트)
fruits = ["apple", "banana", "cherry"]

## 바구니(fruits)에서 하나씩 꺼내서 아래 일을 반복할 수 있다.
for fruit in fruits:
    print(f"내가 좋아하는 과일은 {fruit}입니다.")

for x in fruits:
    print(f"내가 좋아하는 과일은 {x}입니다.")

for item in fruits:
    print(f"내가 좋아하는 과일은 {item}입니다.")

## range()함수: 숫자를 자동으로 만들어주는 도구
for i in range(5): ## 0부터 끝 직전 번호까지
    print(i)

for i in range(1,7): ## 시작부터 끝 직전까지
    print(i)

for i in range(0,10,2): ## 시작부터 끝 직전까지 간격만큼 건너뛰며
    print(i)

## range()는 항상 끝자리 수를 포함하지 않는다