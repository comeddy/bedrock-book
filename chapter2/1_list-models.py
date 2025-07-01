# Python 외부 라이브러리 가져오기
import boto3

# Bedrock 클라이언트 생성
bedrock = boto3.client("bedrock")

# 모델 목록 조회 API 호출
result = bedrock.list_foundation_models()

# 결과를 콘솔에 표시
print(result)
