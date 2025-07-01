# Pyhton 외부 모듈 가져오기
#from anthropic_bedrock import Anthropic

# 클라이언트 생성
#client = AnthropicBedrock()

# 토큰 수 계산 (한국어 문자열)
#tokens = client.count_tokens("Amazon Bedrock은 AWS의 생성형 AI 서비스입니다.")
#print(tokens)

# 토큰 수 계산 (영어 문자열)
#tokens = client.count_tokens("Amazon Bedrock is an AWS generative AI service")
#print(tokens)

import anthropic

client = anthropic.Anthropic()

response = client.messages.count_tokens(
    model="claude-3-7-sonnet-20250219",
    messages=[{
        "role": "user",
        "content": "Hello, Claude"
    }],
)

print(response)

## 코드 수정 필요