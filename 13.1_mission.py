import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 체인 구성
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

prompt = PromptTemplate(
    input_variables=["title"],
    template="""
    다음은 Anthropic 엔지니어링 블로그 글 제목입니다.
    제목: {title}

    이 글이 어떤 내용일지 비전공자도 이해할 수 있게 한 문장으로 요약해주세요.
    """
)

parser = StrOutputParser()
chain = prompt | llm | parser

# 이전에 수집한 JSON 파일 읽기
with open("anthropic_engineering.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

print(f"총 {len(articles)}개 글 요약 시작!\n")
print("=" * 50)

# 각 글 제목을 체인에 넣어서 요약
for i, article in enumerate(articles):
    title = article["title"]
    summary = chain.invoke({"title": title})

    print(f"[{i+1}] {title}")
    print(f">> {summary}")
    print()