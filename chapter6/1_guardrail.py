# 파이썬 외부 라이브러리 가져오기
import json
import boto3

# Bedrock 클라이언트 생성하기
bedrock_runtime = boto3.client("bedrock-runtime")

# 요청 Body 정의
body = json.dumps(
   {
       "anthropic_version": "bedrock-2023-05-31",
       "max_tokens": 1024,
       "messages": [
           {"role": "user",
            "content": [{"type": "text", "text": "생성형 AI는 무엇인가요?"}]}
       ],
   }
)

# 응답을 정의
response = bedrock_runtime.invoke_model(
   body=body,
   modelId="anthropic.claude-3-sonnet-20240229-v1:0",
   guardrailIdentifier="XXXXXXXXXX", # 여기에 가드레일의 ID를 입력합니다.
   guardrailVersion="1", # 여기에 가드레일 버전을 입력합니다.
)

# 생성된 텍스트를 콘솔에 표시
output = json.loads(response.get("body").read())["content"][0]["text"]
print(output)
