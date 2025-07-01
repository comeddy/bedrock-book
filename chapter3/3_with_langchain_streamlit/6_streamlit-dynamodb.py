# Pyhton 외부 모듈 가져오기
import streamlit as st
from langchain_aws import ChatBedrock
from langchain_community.chat_message_histories import DynamoDBChatMessageHistory
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 제목
st.title("Bedrock 채팅")

# 세션 ID 정의
if "session_id" not in st.session_state:
    st.session_state.session_id = "session_id"

# 세션에 대화 기록 설정하기 (이력 정의)
if "history" not in st.session_state:
    st.session_state.history = DynamoDBChatMessageHistory(
        table_name="BedrockChatSessionTable", session_id=st.session_state.session_id
    )

# 세션에 Chain 정의
if "chain" not in st.session_state:
    # 프롬프트 생성
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "당신의 역할은 사용자의 질문에 명확하게 답변하는 것입니다."),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="human_message"),
        ]
    )

    # ChatBedrock 생성
    chat = ChatBedrock(
        model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
        model_kwargs={"max_tokens": 1000},
        streaming=True,
    )

    # Chain 생성
    chain = prompt | chat
    st.session_state.chain = chain

# 대화 기록 삭제 버튼을 화면에 표시
if st.button("대화 기록 삭제"):
    st.session_state.history.clear()

# 메시지를 화면에 출력하기
for message in st.session_state.history.messages:
    with st.chat_message(message.type):
        st.markdown(message.content)

# 채팅 입력란 정의
if prompt := st.chat_input("무엇이든 물어보세요."):
    # 사용자가 입력한 내용을 대화 내역(메시지)에 추가하기
    with st.chat_message("user"):
        st.markdown(prompt)

    # 모델을 실행하고 결과를 화면에 출력하기
    with st.chat_message("assistant"):
        response = st.write_stream(
            st.session_state.chain.stream(
                {
                    "messages": st.session_state.history.messages,
                    "human_message": [HumanMessage(content=prompt)],
                },
                config={"configurable": {"session_id": st.session_state.session_id}},
            )
        )

    # 대화 기록에 추가하기
    st.session_state.history.add_user_message(prompt)
    st.session_state.history.add_ai_message(response)
