# Pyhton 외부 모듈 가져오기
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage

# ChatBedrock 생성
chat = ChatBedrock(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000},
)

# 메세지 정의
messages = [
    SystemMessage(content="당신의 태스크는 사용자의 질문에 명확하게 답변하는 것입니다."),
    HumanMessage(content="하늘이 파란 이유는 무엇입니까?"),
]

# 모델 호출
response = chat.invoke(messages)

print(response.content)
