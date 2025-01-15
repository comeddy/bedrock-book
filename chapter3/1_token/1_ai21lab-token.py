# Pyhton 외부 모듈 가져오기
from ai21_tokenizer import Tokenizer

# 토크나이저 생성
tokenizer = Tokenizer.get_tokenizer()

text = "Amazon Bedrock은 AWS의 생성형 AI 서비스입니다."

# 토크나이저를 사용하여 텍스트 인코딩
encoded_text = tokenizer.encode(text)
# 인코딩 된 텍스트를 토큰별로 분할
tokens = tokenizer.convert_ids_to_tokens(encoded_text)

print(tokens)
