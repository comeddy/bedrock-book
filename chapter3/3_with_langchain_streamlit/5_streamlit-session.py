# Pyhton 외부 모듈 가져오기
import streamlit as st
from langchain_aws import ChatBedrock
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# 제목
st.title("Bedrock 채팅")

# ChatBedrock 생성
chat = ChatBedrock(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    model_kwargs={"max_tokens": 1000},
    streaming=True,
)

# 세션에 메시지 설정하기(정의하기)
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="당신의 역할은 사용자의 질문에 명확하게 답변하는 것입니다."),
    ]

# 메시지를 화면에 출력
for message in st.session_state.messages:
    if message.type != "system":
        with st.chat_message(message.type):
            st.markdown(message.content)

# 채팅 입력란 정의
if prompt := st.chat_input("무엇이든 물어보세요"):
    # 사용자가 입력한 내용을 대화 기록(메시지)에 추가
    st.session_state.messages.append(HumanMessage(content=prompt))

    # 사용자의 입력을 화면에 표시
    with st.chat_message("user"):
        st.markdown(prompt)

    # 모델을 실행하고 결과를 화면에 출력
    with st.chat_message("assistant"):
        response = st.write_stream(chat.stream(st.session_state.messages))
        
    # 모델 호출 결과를 대화 기록에 추가
    st.session_state.messages.append(AIMessage(content=response))
