import asyncio
import os

from dotenv import load_dotenv
from strands import Agent
from strands.models.openai import OpenAIModel

MODEL_ID = "openai.gpt-oss-20b-1:0"
load_dotenv(override=True)


async def main() -> None:
    model = OpenAIModel(
        client_args={
            "base_url": "https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1",
            "api_key": os.getenv("AWS_BEARER_TOKEN_BEDROCK"),
        },
        # **model_config
        model_id=MODEL_ID,
        params={
            "max_completion_tokens": 1024,
            "temperature": 1.0,
            "top_p": 1.0,
            "reasoning_effort": "medium",
        },
    )
    agent = Agent(
        model=model,
        system_prompt="質問に対して日本語で回答してください。",
        callback_handler=None,
    )
    response = agent.stream_async("3.11と3.9はどちらが大きいですか？")

    async for event in response:
        if "data" in event:
            if "<reasoning>" not in event["data"]:
                print(event["data"], end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())
