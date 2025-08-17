import os
import re

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)

client = OpenAI(
    base_url="https://bedrock-runtime.us-west-2.amazonaws.com/openai/v1",
    api_key=os.getenv("AWS_BEARER_TOKEN_BEDROCK"),
)


def main():
    model_id = "openai.gpt-oss-20b-1:0"
    messages = [
        {"role": "developer", "content": "質問に対して日本語で回答してください。"},
        {
            "role": "user",
            "content": "3.11と3.9はどちらが大きいですか？",
        },
    ]

    response = client.chat.completions.create(
        model=model_id,
        messages=messages,
        max_completion_tokens=1024,
        temperature=0.7,
        top_p=0.9,
        reasoning_effort="high",
    )

    content = response.choices[0].message.content
    text = re.sub(r"<reasoning>.*</reasoning>", "", content)
    print(text)
    # print(content)


if __name__ == "__main__":
    main()
