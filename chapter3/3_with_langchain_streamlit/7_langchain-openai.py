# Pyhton 외부 모듈 가져오기
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

# ChatOpenAI 생성
chat = ChatOpenAI(
    openai_api_key="sk-**********",
    model_name="gpt-3.5-turbo-0125",
)

# 메시지 정의
messages = [
    SystemMessage(content="당신의 태스크는 사용자의 질문에 명확하게 답변하는 것입니다."),
    HumanMessage(content="하늘이 파란 이유는 무엇입니까?"),
]

# 모델 호출
response = chat.invoke(messages)

print(response.content)
