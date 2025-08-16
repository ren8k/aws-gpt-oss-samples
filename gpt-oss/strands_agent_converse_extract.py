import asyncio

from strands import Agent
from strands.models import BedrockModel

model = BedrockModel(
    model_id="openai.gpt-oss-20b-1:0",
    # streaming=True,
    params={"temperature": 0.7},
    additional_request_fields={"reasoning_effort": "low"},
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
    async for chunk in agent_stream:
        if "data" in chunk:
            # いい感じにreasoningTextとdataでレスポンスを分けてくれてる．
            print(chunk["data"], end="", flush=True)
        # if "event" in chunk:
        #     event = chunk["event"]
        #     if "contentBlockDelta" in event:
        #         delta = event["contentBlockDelta"]["delta"]
        #         if "text" in delta:
        #             print(delta["text"], end="", flush=True)


# 非同期関数を実行
asyncio.run(process_streaming_response())
