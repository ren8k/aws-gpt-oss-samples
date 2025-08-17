import os
import re

from dotenv import load_dotenv
from openai import OpenAI

MODEL_ID = "openai.gpt-oss-20b-1:0"
load_dotenv(override=True)


def main() -> None:
    client = OpenAI(
        base_url="https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1",
        api_key=os.getenv("AWS_BEARER_TOKEN_BEDROCK"),
    )
    messages = [
        {"role": "developer", "content": "質問に対して日本語で回答してください。"},
        {
            "role": "user",
            "content": "3.11と3.9はどちらが大きいですか？",
        },
    ]

    response = client.chat.completions.create(
        model=MODEL_ID,
        messages=messages,
        max_completion_tokens=1024,
        temperature=1.0,
        top_p=1.0,
        reasoning_effort="medium",
    )

    content = response.choices[0].message.content
    text = re.sub(r"<reasoning>.*?</reasoning>", "", content, flags=re.DOTALL)
    print(text)


if __name__ == "__main__":
    main()
