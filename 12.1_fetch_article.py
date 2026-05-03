import requests
from bs4 import BeautifulSoup
import json

def fetch_article(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    
    response = requests.get(url, headers=headers)
    print(f"상태 코드: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 제목
    title = soup.find(["h1", "h2"])
    title_text = title.get_text(strip=True) if title else "제목 없음"
    
    # 본문 (p 태그 전체 수집)
    paragraphs = soup.find_all("p")
    content = "\n\n".join([p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)])
    
    return {
        "title": title_text,
        "url": url,
        "content": content
    }

url = "https://www.anthropic.com/engineering/building-effective-agents"
article = fetch_article(url)

print(f"\n제목: {article['title']}")
print(f"\n본문 길이: {len(article['content'])}자")
print(f"\n--- 본문 미리보기 (앞 500자) ---")
print(article['content'][:500])

# JSON으로 저장
with open("article_raw.json", "w", encoding="utf-8") as f:
    json.dump(article, f, ensure_ascii=False, indent=2)

print("\n✅ article_raw.json 저장 완료!")