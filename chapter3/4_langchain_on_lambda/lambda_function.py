# Pyhton 외부 모듈 가져오기
from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage, SystemMessage


# Bedrock 호출 함수
def invoke_bedrock(prompt: str):
    # ChatBedrock 생성
    chat = ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        model_kwargs={"max_tokens": 1000},
    )

    # 메시지 정의
    messages = [
        SystemMessage(content="당신의 역할은 사용자의 질문에 명확하게 답하는 것입니다."),
        HumanMessage(content=prompt),
    ]

    # 모델 호출
    response = chat.invoke(messages)
    return response.content

# Lambda 실행 시 호출되는 함수
def lambda_handler(event, context):
    result = invoke_bedrock("하늘이 파란 이유는 무엇입니까？")
    return {"statusCode": 200, "body": result}
