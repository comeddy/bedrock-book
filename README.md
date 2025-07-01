# AWS Bedrock Integration with LangChain and Streamlit

AWS Bedrock, LangChain, Streamlit을 사용해 AI 기반 애플리케이션을 구축하기 위한 포괄적인 툴킷입니다. 이 프로젝트는 텍스트 생성, RAG(검색 증강 생성), 에이전트 및 AWS 단계 함수를 사용한 워크플로 자동화를 위해 바로 사용할 수 있는 예제를 제공합니다.

이 프로젝트는 다음과 같은 실제 구현을 보여줍니다:
- AWS Bedrock 파운데이션 모델과 직접 상호작용
- 고급 AI 기능을 위한 LangChain과 AWS Bedrock의 통합
- Streamlit을 사용한 대화형 웹 인터페이스 구축
- 지식 기반 응답을 위한 RAG 패턴 구현하기
- 특정 기능을 갖춘 AI 에이전트 생성
- AWS 단계 함수를 사용한 AI 워크플로우 오케스트레이션

## Repository Structure
```
.
├── chapter2/                      # Basic AWS Bedrock interactions
│   ├── 1_list-models.py          # List available foundation models
│   ├── 2_invoke-model.py         # Direct model invocation examples
│   ├── 3_streaming.py            # Streaming responses from models
│   └── 4_multimodal.py          # Multimodal capabilities (text + image)
├── chapter3/                      # LangChain integration examples
│   ├── 1_token/                  # Token handling utilities
│   ├── 3_with_langchain_streamlit/ # LangChain + Streamlit integration
│   └── 4_langchain_on_lambda/    # Deploying LangChain on AWS Lambda
├── chapter4/                      # RAG implementation
│   ├── 1_rag.py                  # Basic RAG pattern implementation
│   └── 2_rag-boto3.py           # RAG with AWS SDK integration
├── chapter5/                      # AI Agents and APIs
│   ├── 1_langchain-agent.py      # Basic LangChain agent setup
│   └── 7_agent-for-bedrock.py   # Bedrock-specific agent implementation
├── chapter6/                      # AI guardrails
│   └── 1_guardrail.py           # Implementation of AI safety guardrails
├── chapter8/                      # Advanced workflows
│   ├── 1_model-parameters/       # Model configuration templates
│   ├── 2_vscode/                 # VS Code integration
│   └── Bedrock-StateMachine.asl.yaml # Step Functions workflow definition
└── docs/                         # Documentation and diagrams
```

## Usage Instructions
### Prerequisites
- Python 3.7+
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials
- Required Python packages:
  - boto3
  - langchain
  - streamlit
  - python-dateutil

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r chapter3/3_with_langchain_streamlit/requirements.txt
```

### Quick Start
1. Run a simple Streamlit:
```python
streamlit run chapter2/3_streaming.py
```

2. Bedrock 모델활성 및 실습방법은 2장(2.11) 참고해주세요.
 

### More Detailed Examples
1. Using LangChain with Bedrock:
```python
from langchain_aws import BedrockChat
from langchain_core.messages import HumanMessage, SystemMessage

chat = BedrockChat(
    model_id="anthropic.claude-3-sonnet-20240229-v1:0",
    model_kwargs={"max_tokens": 1000}
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Why is the sky blue?")
]
response = chat(messages)
print(response.content)
```

2. Implementing RAG pattern:
```python
from langchain_aws import BedrockChat
from langchain_core.prompts import ChatPromptTemplate

# Initialize retriever and model
retriever = AmazonKnowledgeBasesRetriever(
    knowledge_base_id="your-kb-id",
    retrieval_config={"vectorSearchConfiguration": {}}
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer based on the following context:\n\n{context}"),
    ("human", "{question}")
])

# Create chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)
```

## Data Flow
The project implements a layered architecture for AI interactions:
1. Foundation layer: Direct AWS Bedrock API interactions
2. Integration layer: LangChain abstractions and utilities
3. Application layer: Streamlit web interfaces

Key component interactions:
- 사용자 인터페이스 및 세션 관리를 처리하는 Streamlit
- AI 운영을 위한 높은 수준의 추상화를 제공하는 LangChain
- 기초 모델 기능을 제공하는 AWS Bedrock
- 복잡한 워크플로우를 오케스트레이션하는 Step Functions
- DynamoDB는 대화 기록을 저장합니다(구성 시).
