# Python 외부 라이브러리 가져오기
import json
import boto3

# Bedrock 클라이언트 생성
bedrock_runtime = boto3.client("bedrock-runtime")

# 요청 본문 정의
body = json.dumps(
    {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1000,
        "messages": [
            {"role": "user", "content": [{"type": "text", "text": "아이유 노래를 알려주세요"}]}
        ],
    }
)

# 모델 정의 (Claude 3 Sonnet)
modelId = "anthropic.claude-3-sonnet-20240229-v1:0"

# 응답 정의
response = bedrock_runtime.invoke_model_with_response_stream(body=body, modelId=modelId)

# 스트리밍 출력
for event in response.get("body"):
    chunk = json.loads(event["chunk"]["bytes"])
    if (
        chunk["type"] == "content_block_delta"
        and chunk["delta"]["type"] == "text_delta"
    ):
        print(chunk["delta"]["text"], end="")

# 스트리밍 종료 후 줄바꿈
print()
