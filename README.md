# MCP-demo — MCP Client with LangGraph + Groq

A demo project showing how to connect a LangGraph agent to multiple MCP (Model Context Protocol) servers — a local math server (stdio) and a weather server (streamable HTTP) — using [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain-mcp-adapters) and Groq as the LLM backend.

## Features

- Connects to multiple MCP servers simultaneously (stdio + HTTP transports)
- Uses LangGraph's React agent to reason over tool calls
- Powered by Groq for fast inference

## Project Structure

.
├── client.py # Main client — connects to MCP servers and runs the agent
├── mathserver.py # MCP server exposing math tools (stdio transport)
├── weather.py # MCP server exposing weather tools (streamable HTTP transport)
├── .env # API keys (not committed — see .gitignore)
├── pyproject.toml
└── requirements.txt


## Setup

1. Clone the repo:
```bash
   git clone https://github.com/veenzzzz/Rag-demo.git
   cd Rag-demo
```

2. Create a virtual environment and install dependencies:
```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Groq API key:

GROQ_API_KEY=your_key_here


## Running

You need **two terminals** open at the same time:

**Terminal 1 — start the weather server:**
```bash
python weather.py
```

**Terminal 2 — run the client:**
```bash
python client.py
```

The math server (`mathserver.py`) is launched automatically by `client.py` over stdio — no separate terminal needed for it.

## Example

math_response: The weather in California right now is: "It's always raining in California."
And the answer to 2 + 2 is 4.


## Notes

- Model used: `openai/gpt-oss-120b` (or swap for any current Groq-supported model — check [Groq's model list](https://console.groq.com/docs/models)).
- Never commit `.env` — it's excluded via `.gitignore`.
