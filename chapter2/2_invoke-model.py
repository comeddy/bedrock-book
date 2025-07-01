# Python 외부 라이브러리 가져오기
import json
import boto3

#Bedrock 클라이언트 생성
bedrock = boto3.client("bedrock-runtime")

# 요청 본문 정의
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {
                "role": "user",
                "content": "Bedrock은 무슨 뜻인가요?",
            }
        ],
    }
)

# 모델 정의 (Claude 3 Sonnet)
modelId = "anthropic.claude-3-5-sonnet-20240620-v1:0"

# HTTP 헤더 정의
accept = "application/json"
contentType = "application/json"

# 응답 정의
response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
response_body = json.loads(response.get("body").read())
answer = response_body["content"][0]["text"]

# 생성된 텍스트를 콘솔에 표시합니다.
print(answer)
