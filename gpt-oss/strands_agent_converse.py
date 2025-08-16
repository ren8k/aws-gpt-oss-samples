from strands import Agent
from strands.models import BedrockModel

model = BedrockModel(
    model_id="openai.gpt-oss-20b-1:0",
    streaming=True,
    params={"temperature": 0.7},
    additional_request_fields={"reasoning_effort": "high"},
)

agent = Agent(
    model=model,
    system_prompt="質問に対して日本語で回答してください。",
)
agent("3.11と3.9はどちらが大きいですか？")
