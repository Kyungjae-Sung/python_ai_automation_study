import requests
from bs4 import BeautifulSoup
import json

def get_anthropic_engineering_posts():
    url = "https://www.anthropic.com/engineering"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    
    response = requests.get(url, headers=headers)
    print(f"상태 코드: {response.status_code}")
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    articles = []
    
    # <a> 태그 중 /engineering/으로 시작하는 링크만 찾기
    links = soup.find_all("a", href=True)
    
    for link in links:
        href = link.get("href", "")
        
        # 엔지니어링 블로그 글 링크만 필터링
        if href.startswith("/engineering/") and href != "/engineering":
            
            # 제목 찾기 (h2 또는 h3 태그)
            title_tag = link.find(["h2", "h3"])
            title = title_tag.get_text(strip=True) if title_tag else ""
            
            # 날짜 찾기 (텍스트에서 날짜 형식 탐색)
            text_content = link.get_text(separator=" ", strip=True)
            
            if title:  # 제목이 있는 경우만 추가
                article = {
                    "title": title,
                    "link": "https://www.anthropic.com" + href,
                    "text_preview": text_content[:200]
                }
                # 중복 제거
                if not any(a["link"] == article["link"] for a in articles):
                    articles.append(article)
    
    return articles

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n✅ {filename} 저장 완료!")

# 실행
posts = get_anthropic_engineering_posts()
print(f"\n총 {len(posts)}개의 글을 찾았어요!\n")

for i, post in enumerate(posts):
    print(f"[{i+1}] {post['title']}")
    print(f"     {post['link']}")
    print()

save_to_json(posts, "anthropic_engineering.json")