import asyncio

from strands import Agent
from strands.models import BedrockModel

MODEL_ID = "openai.gpt-oss-20b-1:0"


async def main() -> None:
    model = BedrockModel(
        model_id=MODEL_ID,
        params={"temperature": 1.0, "top_p": 1.0},
        additional_request_fields={"reasoning_effort": "medium"},
    )
    agent = Agent(
        model=model,
        system_prompt="質問に対して日本語で回答してください。",
        callback_handler=None,
    )
    response = agent.stream_async("3.11と3.9はどちらが大きいですか？")

    async for chunk in response:
        if "data" in chunk:
            # Strands splits the response into reasoningText and data.
            print(chunk["data"], end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
