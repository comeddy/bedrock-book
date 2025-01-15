# Pyhton 외부 모듈 가져오기
from ai21_tokenizer import Tokenizer

# 토크나이저 생성
tokenizer = Tokenizer.get_tokenizer()

# 토크나이저로 인코딩 하고 토큰 수 출력 (한국어 문자열)
encoded_text = tokenizer.encode("Amazon Bedrock은 AWS의 생성형 AI 서비스입니다.")
print(len(encoded_text))

# 토크나이저로 인코딩 하고 토큰 수 출력 (영어 문자열)
encoded_text = tokenizer.encode("Amazon Bedrock is an AWS generative AI service")
print(len(encoded_text))
