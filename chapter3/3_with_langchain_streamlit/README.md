# 3.5 3.5.	LangChain과 Streamlit을 이용한 생성형 AI 앱 개발 (p.154)

## Claude 3.5 Sonnet 에의 대응 (을 사용할 경우)

제2장의 p.80을 참고하여 Anthropic사의 'Claude 3.5 Sonnet' 모델을 활성화해 주세요.

소스코드에서`model_id`를 `anthropic.claude-3-5-sonnet-20240620-v1:0`로 변경합니다. 라이브러리의 버전을 업데이트할 필요는 없습니다.

* 변경 전
    ```python
    # ChatBedrockを生成
    chat = ChatBedrock(
        model_id="anthropic.claude-3-sonnet-20240229-v1:0",
        model_kwargs={"max_tokens": 1000},
    )
    ```

* 변경 후
    ```python
    # ChatBedrockを生成
    chat = ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        model_kwargs={"max_tokens": 1000},
    )
    ```
