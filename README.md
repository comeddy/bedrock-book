# Amazon Bedrock 생성형 AI 앱 개발 입문

Amazon Bedrock, LangChain, Streamlit을 활용한 생성형 AI 애플리케이션 개발을 위한 실습 코드 저장소입니다. 이 프로젝트는 Amazon Bedrock의 파운데이션 모델을 활용하여 텍스트 생성, RAG(검색 증강 생성), AI 에이전트, 워크플로 자동화까지 다양한 생성형 AI 기능을 구현하는 방법을 제공합니다.

## 📚 프로젝트 개요

이 저장소는 다음과 같은 실제 구현 예제를 포함합니다:
- Amazon Bedrock 파운데이션 모델과의 직접 상호작용
- LangChain을 통한 고급 AI 기능 구현
- Streamlit을 사용한 대화형 웹 인터페이스 구축
- RAG 패턴을 통한 지식 기반 응답 시스템
- 특정 기능을 갖춘 AI 에이전트 개발
- AWS Step Functions를 활용한 AI 워크플로 오케스트레이션

## 🗂️ 저장소 구조

```
bedrock-book/
├── chapter2/                          # Amazon Bedrock 기본 사용법
│   ├── 1_list-models.py              # 사용 가능한 파운데이션 모델 목록 조회
│   ├── 2_invoke-model.py             # 모델 직접 호출 예제
│   ├── 3_streaming.py                # 스트리밍 응답 처리
│   ├── 4_multimodal.py               # 멀티모달 기능 (텍스트 + 이미지)
│   ├── image.png                     # 테스트용 이미지 파일
│   └── image-kr.png                  # 한국어 테스트용 이미지 파일
├── chapter3/                          # LangChain 통합 예제
│   ├── 1_token/                      # 토큰 처리 유틸리티
│   │   ├── 1_ai21lab-token.py        # AI21 Labs 토큰 처리
│   │   ├── 2_anthropic-token-count.py # Anthropic 토큰 카운팅
│   │   └── 3_ai21lab-token-count.py  # AI21 Labs 토큰 카운팅
│   ├── 3_with_langchain_streamlit/   # LangChain + Streamlit 통합
│   │   ├── 1_langchain.py            # 기본 LangChain 사용법
│   │   ├── 2_langchain-debug.py      # 디버깅 모드
│   │   ├── 3_langchain-streaming.py  # 스트리밍 처리
│   │   ├── 4_streamlit.py            # Streamlit 웹 앱
│   │   ├── 5_streamlit-session.py    # 세션 관리
│   │   ├── 6_streamlit-dynamodb.py   # DynamoDB 연동
│   │   └── requirements.txt          # 필요한 패키지 목록
│   └── 4_langchain_on_lambda/        # AWS Lambda에서 LangChain 실행
│       └── lambda_function.py        # Lambda 함수 코드
├── chapter4/                          # RAG (검색 증강 생성) 구현
│   ├── 1_rag.py                      # 기본 RAG 패턴 구현
│   ├── 2_rag-boto3.py               # AWS SDK를 활용한 RAG
│   └── requirements.txt              # 필요한 패키지 목록
├── chapter5/                          # AI 에이전트 및 API 연동
│   ├── 1_langchain-agent.py          # 기본 LangChain 에이전트
│   ├── 2_langchain-react-agent.py    # ReAct 패턴 에이전트
│   ├── 3_agent-prompt.txt            # 에이전트 프롬프트 템플릿
│   ├── 4_openapi.yaml               # OpenAPI 스펙 정의
│   ├── 5_get-awsblog-post.py        # AWS 블로그 포스트 수집
│   ├── 6_knowledgebase-prompt.txt    # 지식 베이스 프롬프트
│   ├── 7_agent-for-bedrock.py       # Bedrock 전용 에이전트
│   ├── 8_action-group-function.json  # 액션 그룹 함수 정의
│   ├── 9_get-awsblog-postv2.py     # AWS 블로그 포스트 수집 v2
│   └── requirements.txt              # 필요한 패키지 목록
├── chapter6/                          # AI 가드레일 (안전장치)
│   └── 1_guardrail.py               # AI 안전장치 구현
├── chapter8/                          # 고급 워크플로 및 자동화
│   ├── 1_model-parameters/           # 모델 파라미터 템플릿
│   │   ├── 1_게시물_요약.json        # 게시물 요약 파라미터
│   │   ├── 2_자기소개문과_캐치프레이즈_작성.json # 자기소개 작성 파라미터
│   │   ├── 3_Markdown_형식_변환.json  # Markdown 변환 파라미터
│   │   ├── 4_이미지_생성용_프롬프트_작성.json # 이미지 생성 프롬프트 파라미터
│   │   └── 5_썸네일_이미지_생성.json   # 썸네일 생성 파라미터
│   ├── 2_vscode/                     # VS Code 통합
│   │   ├── 1_stepfunctions.py        # Step Functions 실행
│   │   └── requirements.txt          # 필요한 패키지 목록
│   └── Bedrock-StateMachine.asl.yaml # Step Functions 워크플로 정의
├── docs/                             # 문서 및 다이어그램
│   ├── infra.dot                     # 인프라 구조도 (DOT 형식)
│   └── infra.svg                     # 인프라 구조도 (SVG 형식)
├── images/                           # 이미지 리소스
│   └── flyer.png                     # 플라이어 이미지
├── pdf/                              # 참고 문서
│   ├── [샘플] 광고1번지 2021년 12월호(펼침).pdf
│   └── s3-optimizing-performance-best-practices.pdf
├── .gitignore                        # Git 무시 파일 목록
├── LICENSE                           # 라이선스 파일
└── README.md                         # 이 파일
```

## 🚀 시작하기

### 사전 요구사항

- Python 3.8 이상
- AWS 계정 및 Bedrock 액세스 권한
- AWS CLI 구성 완료
- 필요한 Python 패키지들

### 설치 방법

1. **저장소 클론**
   ```bash
   git clone https://github.com/comeddy/bedrock-book.git
   cd bedrock-book
   ```

2. **가상 환경 생성 및 활성화**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **의존성 설치**
   ```bash
   # 기본 패키지 설치
   pip install boto3 langchain streamlit python-dateutil
   
   # 특정 챕터별 요구사항 설치
   pip install -r chapter3/3_with_langchain_streamlit/requirements.txt
   pip install -r chapter4/requirements.txt
   pip install -r chapter5/requirements.txt
   ```

### Amazon Bedrock 모델 활성화

1. AWS 콘솔에서 Amazon Bedrock 서비스로 이동
2. 좌측 메뉴에서 "Model access" 선택
3. 사용하고자 하는 모델들을 활성화:
   - Anthropic Claude 3 Sonnet
   - Anthropic Claude 3.5 Sonnet
   - AI21 Labs Jurassic-2 모델들
   - Amazon Titan 모델들

## 📖 사용 예제

### 1. 기본 모델 호출 (Chapter 2)

```python
# 사용 가능한 모델 목록 확인
python chapter2/1_list-models.py

# 모델 직접 호출
python chapter2/2_invoke-model.py

# 스트리밍 응답 처리
python chapter2/3_streaming.py
```

### 2. LangChain과 Streamlit 통합 (Chapter 3)

```python
# Streamlit 웹 앱 실행
streamlit run chapter3/3_with_langchain_streamlit/4_streamlit.py

# 세션 관리가 포함된 앱 실행
streamlit run chapter3/3_with_langchain_streamlit/5_streamlit-session.py
```

### 3. RAG 시스템 구현 (Chapter 4)

```python
# 기본 RAG 패턴
python chapter4/1_rag.py

# AWS SDK를 활용한 RAG
python chapter4/2_rag-boto3.py
```

### 4. AI 에이전트 개발 (Chapter 5)

```python
# 기본 LangChain 에이전트
python chapter5/1_langchain-agent.py

# ReAct 패턴 에이전트
python chapter5/2_langchain-react-agent.py

# Bedrock 전용 에이전트
python chapter5/7_agent-for-bedrock.py
```

## 🔧 주요 기능

### 1. 파운데이션 모델 활용
- **텍스트 생성**: Claude, Jurassic-2 등 다양한 모델 지원
- **멀티모달**: 텍스트와 이미지를 함께 처리
- **스트리밍**: 실시간 응답 처리

### 2. LangChain 통합
- **체인 구성**: 복잡한 AI 워크플로 구축
- **메모리 관리**: 대화 컨텍스트 유지
- **프롬프트 템플릿**: 재사용 가능한 프롬프트 관리

### 3. 웹 인터페이스
- **Streamlit**: 직관적인 웹 UI 제공
- **세션 관리**: 사용자별 대화 상태 유지
- **DynamoDB 연동**: 대화 기록 영구 저장

### 4. RAG 시스템
- **문서 검색**: 관련 문서 자동 검색
- **컨텍스트 증강**: 검색된 정보를 활용한 답변 생성
- **지식 베이스**: AWS Knowledge Base 연동

### 5. AI 에이전트
- **도구 사용**: 외부 API 및 함수 호출
- **추론 과정**: ReAct 패턴을 통한 단계별 사고
- **액션 그룹**: Bedrock Agent의 고급 기능 활용

## 🛠️ 고급 설정

### Claude 3.5 Sonnet 사용

최신 Claude 3.5 Sonnet 모델을 사용하려면 다음과 같이 모델 ID를 변경하세요:

```python
# 기존
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

# 변경 후
model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
```

### DynamoDB 설정

대화 기록을 저장하려면 DynamoDB 테이블을 생성하세요:

```bash
aws dynamodb create-table \
    --table-name ChatHistory \
    --attribute-definitions \
        AttributeName=SessionId,AttributeType=S \
    --key-schema \
        AttributeName=SessionId,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST
```

### Step Functions 워크플로

복잡한 AI 워크플로를 자동화하려면 `chapter8/Bedrock-StateMachine.asl.yaml` 파일을 사용하여 Step Functions를 배포하세요.

## 📊 아키텍처

이 프로젝트는 다음과 같은 계층화된 아키텍처를 구현합니다:

1. **기반 계층**: Amazon Bedrock API 직접 호출
2. **통합 계층**: LangChain 추상화 및 유틸리티
3. **애플리케이션 계층**: Streamlit 웹 인터페이스
4. **오케스트레이션 계층**: Step Functions 워크플로

주요 컴포넌트 간 상호작용:
- **Streamlit**: 사용자 인터페이스 및 세션 관리
- **LangChain**: AI 작업을 위한 고수준 추상화
- **Amazon Bedrock**: 파운데이션 모델 기능 제공
- **Step Functions**: 복잡한 워크플로 오케스트레이션
- **DynamoDB**: 대화 기록 저장 (선택사항)

## 🤝 기여하기

1. 이 저장소를 포크합니다
2. 새로운 기능 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`)
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`)
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`)
5. Pull Request를 생성합니다

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.

## 🆘 지원 및 문의

- **이슈 리포팅**: [GitHub Issues](https://github.com/comeddy/bedrock-book/issues)
- **문서**: 각 챕터별 README 파일 참조
- **예제**: 각 Python 파일의 주석 참조

## 📚 참고 자료

- [Amazon Bedrock 공식 문서](https://docs.aws.amazon.com/bedrock/)
- [LangChain 공식 문서](https://python.langchain.com/)
- [Streamlit 공식 문서](https://docs.streamlit.io/)
- [AWS Step Functions 공식 문서](https://docs.aws.amazon.com/step-functions/)

---

**주의**: 이 코드를 실행하기 전에 Amazon Bedrock에서 필요한 모델들을 활성화했는지 확인하세요. 일부 모델은 사용 승인이 필요할 수 있습니다.
