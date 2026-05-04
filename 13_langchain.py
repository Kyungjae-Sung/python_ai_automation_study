import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 블록 1: LLM (AI model)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# 블록 2: PromptTemplate (프롬프트 틀)
prompt = PromptTemplate(
    input_variables=["topic"],
    template="'{topic}'를 입문자도 이해할 수 있게 한 문장으로 설명해주세요"
)

# 블록 3: OutputParser (결과를 문자열로 변환)
parser = StrOutputParser()

# 체인 연결: 블록1 | 블록2 | 블록3
chain = prompt | llm | parser

# 실행
result = chain.invoke({"topic": "RAG"})
print(result)

# topic만 바꿔서 여러 번 재사용
topics = ["LangChain", "벡터 데이터베이스", "임베딩"]

for topic in topics:
    result = chain.invoke({"topic": topic})
    print(f"[{topic}]")
    print(result)
    print()

# 변수 2개짜리 프롬프트
prompt2 = PromptTemplate(
    input_variables=["topic", "audience"],
    template="'{topic}'를 {audience}도 이해할 수 있게 한 문장으로 설명해주세요"
)

chain2 = prompt2 | llm | parser

print(chain2.invoke({"topic": "RAG", "audience": "초등학생"}))
print(chain2.invoke({"topic": "RAG", "audience": "개발자"}))
print(chain2.invoke({"topic": "RAG", "audience": "AI 박사"}))
print(chain2.invoke({"topic": "RAG", "audience": "화가"}))
print(chain2.invoke({"topic": "RAG", "audience": "뇌과학자"}))