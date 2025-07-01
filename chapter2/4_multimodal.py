# Python 외부 라이브러리 가져오기
import base64
import json
import boto3

# Bedrock 호출용 클라이언트 생성
bedrock_runtime = boto3.client("bedrock-runtime")

# 이미지 파일 변환
with open("image-kr.png", "rb") as image_file:
    image_data = base64.b64encode(image_file.read()).decode("utf-8")

# 프롬프트 정의
prompt_config = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 4096,
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {
                        "type": "base64",
                        "media_type": "image/png",
                        "data": image_data,
                    },
                },
                {"type": "text", "text": "이 이미지는 무엇인가요? 한국어로 설명해 주세요"},
            ],
        }
    ],
}

# Bedrock 호출 매개변수 정의
body = json.dumps(prompt_config)
modelId = "anthropic.claude-3-5-sonnet-20240620-v1:0"
accept = "application/json"
contentType = "application/json"

# 응답 받기
response = bedrock_runtime.invoke_model(
    body=body, modelId=modelId, accept=accept, contentType=contentType
)
response_body = json.loads(response.get("body").read())
results = response_body.get("content")[0].get("text")

# 생성된 텍스트를 콘솔로 출력
print(results)
