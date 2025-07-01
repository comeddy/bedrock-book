import nest_asyncio
import streamlit as st
from bs4 import BeautifulSoup
from langchain import hub
from langchain.agents import AgentExecutor, Tool, create_react_agent
from langchain_aws import ChatBedrock
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.messages import HumanMessage, SystemMessage

nest_asyncio.apply()

search = DuckDuckGoSearchRun()
tools = [
    Tool(
        name="duckduckgo-search",
        func=search.run,
        description="이 도구는 사용자로부터 검색 키워드를 받아 웹에서 최신 정보를 검색한다.",
    )
]

# 채팅 모델 설정
chat = ChatBedrock(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    model_kwargs={"max_tokens": 1500},
)

# 에이전트 설정
agent = create_react_agent(chat, tools, prompt=hub.pull("hwchase17/react"))
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)

# Streamlit 애플리케이션 설정
st.title("Bedrock ReAct Agent 채팅")
messages = [SystemMessage(content="질문에 대해서는 반드시 한국어로 답변해 드립니다.")]

# 사용자 입력 처리
prompt = st.chat_input("무엇이든 물어보세요.")
if prompt:
    messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        # 상담원에게 문의하기
        result = agent_executor.invoke({"input": prompt})
        st.write(result["output"])
