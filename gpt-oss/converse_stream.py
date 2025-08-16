import boto3

client = boto3.client("bedrock-runtime", region_name="us-west-2")


def main():
    model_id = "openai.gpt-oss-20b-1:0"
    system = [{"text": "質問に対して日本語で回答してください。"}]
    messages = [
        {
            "role": "user",
            "content": [{"text": "3.11と3.9はどちらが大きいですか？"}],
        }
    ]
    inference_config = {"maxTokens": 1024, "temperature": 0.7, "topP": 0.9}
    additional_confg = {"reasoning_effort": "low"}

    response = client.converse_stream(
        modelId=model_id,
        system=system,
        messages=messages,
        inferenceConfig=inference_config,
        additionalModelRequestFields=additional_confg,
    )

    for chunk in response["stream"]:
        if "contentBlockDelta" in chunk:
            delta = chunk["contentBlockDelta"]["delta"]
            if "text" in delta:
                print(delta["text"], end="", flush=True)


if __name__ == "__main__":
    main()
