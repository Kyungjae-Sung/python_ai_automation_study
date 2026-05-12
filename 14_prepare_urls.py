import json

# 이미 발행된 3개 슬러그
published = [
    "contextual-retrieval",
    "building-effective-agents", 
    "swe-bench-sonnet"
]

# 전체 목록 읽기
with open("anthropic_engineering.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

# 발행 안 된 것만 필터링 (오래된 순으로 역순 정렬)
remaining = []
order = 4

for article in reversed(articles): # 오래된 것부터
    slug = article["link"].split("/")[-1]
    if slug not in published:
        remaining.append({
            "order": order,
            "title": article["title"],
            "url": article["link"],
            "slug": slug
        })

# order 번호 다시 부여
for i, item in enumerate(remaining):
    item["order"] = i + 4

# save
with open("ai_news_urls.json", "w", encoding="utf-8") as f:
    json.dump(remaining, f, ensure_ascii=False, indent=2)

print(f"총 {len(remaining)}개 URL 준비 완료!")
for item in remaining:
    print(f"[{item['order']}] {item['title']}")