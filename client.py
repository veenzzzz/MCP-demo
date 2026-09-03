from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
import asyncio
import os

load_dotenv()


async def main():

    client = MultiServerMCPClient(
        {
            "math": {
                "transport": "stdio",
                "command": "python",
                "args": ["mathserver.py"],
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable-http",
            }
        }
    )

    tools = await client.get_tools()

    model = ChatGroq(model="openai/gpt-oss-120b")

    agent = create_react_agent(model, tools)

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather in California and what is 2+2?"}]}
    )

    print("math_response:", math_response["messages"][-1].content)


asyncio.run(main())