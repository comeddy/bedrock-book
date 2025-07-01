# Python 외부 라이브러리 임포트
import boto3
import streamlit as st

# 프론트엔드 작성
st.title("알려줘! Bedrock")
question = st.text_input("질문 입력")
button = st.button("질문하기")

# Bedrock 클라이언트 생성
kb = boto3.client("bedrock-agent-runtime")

# 버튼이 눌리면 널리지 베이스 호출
if button:
    # 널리지 베이스 정의
    response = kb.retrieve_and_generate(
        input={"text": question},
        retrieveAndGenerateConfiguration={
            "type": "KNOWLEDGE_BASE",
            "knowledgeBaseConfiguration": {
                "knowledgeBaseId": "XXXXXXXXXX",  # 널리지 베이스 ID
                "modelArn": "arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-3-sonnet-20240229-v1:0",
            },
        },
    )

    # RAG 결과를 화면에 표시
    st.write(response["output"]["text"])
