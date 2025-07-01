import uuid

import boto3
import streamlit as st

# Agent의 정의
agent_id: str = "XXXXXXXXXX"  # 에이전트 ID 입력
agent_alias_id: str = "XXXXXXXXXX"  # 별칭 ID 입력
session_id: str = str(uuid.uuid1())
client = boto3.client("bedrock-agent-runtime")

st.title("Agents for Amazon Bedrok 채팅")

if prompt := st.chat_input("무엇이든 물어보세요."):
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Agent 실행
        response = client.invoke_agent(
            inputText=prompt,
            agentId=agent_id,
            agentAliasId=agent_alias_id,
            sessionId=session_id,
            enableTrace=False,
        )

        # Agent 실행 결과 획득
        event_stream = response["completion"]
        text = ""  # text 초기화
        for event in event_stream:
            if "chunk" in event:
                text += event["chunk"]["bytes"].decode("utf-8")
        st.write(text)
