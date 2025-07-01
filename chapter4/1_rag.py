# 외부 라이브러리 임포트
import streamlit as st
from langchain_aws import ChatBedrock
from langchain_aws.retrievers import AmazonKnowledgeBasesRetriever
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

# 검색 방법을 지정
retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="XXXXXXXXXX",  # 여기에는 지식 기반 ID를 입력합니다
    retrieval_config={"vectorSearchConfiguration": {"numberOfResults": 10}},
)

# 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_template(
    "다음의 context에 기반하여 답변해주세요: {context} / 질문: {question}"
)

# LLM 지정
model = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
)

# 체인 정의 (검색 → 프롬프트 생성 → LLM 호출 → 결과 얻기)
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)

# 프론트엔드 작성
st.title("알려줘! Bedrock")
question = st.text_input("질문을 입력하세요")
button = st.button("질문하기")

# 버튼이 눌리면 체인 실행 결과 표시
if button:
    st.write(chain.invoke(question))
