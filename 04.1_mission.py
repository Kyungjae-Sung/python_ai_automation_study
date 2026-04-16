ai_response = {
    "status": "success",
    "score": 92,
    "language": "Korean"
}

if ai_response["status"] == "success":
    print("응답성공")
elif ai_response["status"] == "error":
    print("응답실패, 원인파악후 재시도합니다")
else:
    print("알 수 없는 상태입니다")




if ai_response["score"] >= 90:
    print(f"응답품질: 최상")
elif ai_response["score"] >= 70:
    print(f"응답품질: 양호")
elif ai_response["score"] >= 50:
    print(f"응답품질: 보통")
else:
    print(f"응답품질: 불량")


if ai_response["score"] >= 80 and ai_response["language"] == "Korean":
    print("한국어 고품질 응답입니다")
else:
    print("잘못된 응답입니다")