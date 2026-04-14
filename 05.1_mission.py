news = ["AI 반도체 수출 역대 최고", "오늘 서울 날씨 맑음", "GPT-5 출시 임박", "프로야구 개막전 결과", "LangChain 새 버전 업데이트"]


# for i in range(5):
#     print(f"[{i}] {news[i]}")


print("\n=== AI News ===")
for i in range(len(news)):
    if "AI" in news[i] or "GPT" in news[i] or "LangChain" in news[i]:
        print(f"[{i+1}] {news[i]} <<- AI관련 뉴스!")
    else:
        print(f"[{i+1}] {news[i]}")