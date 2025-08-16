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
    system_prompt="質問に対して日本語で回答してください。必ず論理的に思考せよ．",
)
agent("3.11と3.9はどちらが大きいですか？")
