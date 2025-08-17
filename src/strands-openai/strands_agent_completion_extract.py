import asyncio
import os

from dotenv import load_dotenv
from strands import Agent
from strands.models.openai import OpenAIModel

load_dotenv(override=True)

model = OpenAIModel(
    client_args={
        "base_url": "https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1",
        "api_key": os.getenv("AWS_BEARER_TOKEN_BEDROCK"),
    },
    # **model_config
    model_id="openai.gpt-oss-20b-1:0",
    params={
        "max_completion_tokens": 1000,
        "temperature": 0.7,
        "reasoning_effort": "low",
    },
)

agent = Agent(
    model=model,
    system_prompt="質問に対して日本語で回答してください。",
    callback_handler=None,
)


async def process_streaming_response():
    # stream_async()を使ってチャンクを取得
    agent_stream = agent.stream_async("3.11と3.9はどちらが大きいですか？")

    # 各チャンクを処理
    async for event in agent_stream:
        if "data" in event:
            # テキストチャンクを出力
            if "<reasoning>" not in event["data"]:
                print(event["data"], end="", flush=True)
        # elif "current_tool_use" in event and event["current_tool_use"].get("name"):
        #     # ツール使用情報を出力
        #     print(f"\n[Tool use: {event['current_tool_use']['name']}]")


# 非同期関数を実行
asyncio.run(process_streaming_response())
