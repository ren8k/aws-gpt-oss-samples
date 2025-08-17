import boto3

MODEL_ID = "openai.gpt-oss-20b-1:0"


def main():
    client = boto3.client("bedrock-runtime", region_name="us-west-2")
    system = [{"text": "質問に対して日本語で回答してください。"}]
    messages = [
        {
            "role": "user",
            "content": [{"text": "3.11と3.9はどちらが大きいですか？"}],
        }
    ]
    inference_config = {"maxTokens": 1024, "temperature": 1.0, "topP": 1.0}
    additional_confg = {"reasoning_effort": "medium"}

    response = client.converse(
        modelId=MODEL_ID,
        system=system,
        messages=messages,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_confg,
    )

    for content_block in response["output"]["message"]["content"]:
        if "text" in content_block:
            print(content_block["text"])


if __name__ == "__main__":
    main()
