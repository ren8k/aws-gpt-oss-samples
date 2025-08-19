# AWS GPT-OSS Samples

AWS Bedrock での GPT-OSS モデル使用サンプル集

## 概要

このプロジェクトは，AWS Bedrock で提供される OpenAI GPT-OSS モデルを，以下の API やフレームワークから利用するためのサンプルコードを提供します．なお，非常に簡易的な実装としております．

- [Amazon Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
- [Amazon Bedrock ConverseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
- [OpenAI Completions API](https://platform.openai.com/docs/guides/completions)
- [Strands Agents](https://strandsagents.com/latest/)

## インストール

```bash
# プロジェクトのクローン
git clone https://github.com/ren8k/aws-gpt-oss-samples.git
cd aws-gpt-oss-samples

# 依存関係のインストール
uv sync
```

## 設定

- `.env` ファイルを作成してください．

```
cp .env.example .env
```

- AWS Bedrock のベアラートークンを設定

```
AWS_BEARER_TOKEN_BEDROCK=your_bearer_token_here
```

- 本コードの実行に必要な IAM Role を設定してください．（以下例）

```
AmazonBedrockFullAccess
```

- 以下の Bedrock のモデルを Activate してください． (コードでは `us-west-2` を利用)

```
openai.gpt-oss-120b-1:0
openai.gpt-oss-20b-1:0
```

## サンプルコード

### ディレクトリ構成

```
src/
  ├── bedrock-completion/: OpenAI Completions API を利用
  ├── bedrock-converse/  : Bedrock Converse API / Bedrock ConverseStream API を利用
  ├── strands-bedrock/   : Strands Agent (strands.models.BedrockModel) を利用
  └── strands-openai/    : Strands Agent (strands.models.OpenAIModel) を利用
```

### モデル設定

- 使用しているモデル: `openai.gpt-oss-20b-1:0`
- 主な設定パラメータ([公式](https://github.com/openai/gpt-oss)推奨値):
  - `max_completion_tokens`: 1024
  - `temperature`: 1.0
  - `top_p`: 1.0
  - `reasoning_effort`: "medium"

## Tips

Strands Agents の `strands.models.OpenAIModel` の内部実装では， OpenAI Completions API が利用されています．ですので，`src/bedrock-completion/completion_stream.py` と `src/strands-openai/strands_agent_completion_extract.py` のレスポンスの形式はほぼ同じです．

## 既知の問題

Converse API 実行時，response の text フィールドにおいて，Reasoning word と最終的な回答が混在することがあります．具体的には，text フィールド中に `<reasoning>` タグを含む回答が混ざることがあります．これは API 側のバグと思われますが，現時点（2025/08/19）では `<reasoning>` タグを除去する処理を追加実装する必要があるかもしれません．

一方，Completions API 実行時，response の data フィールドにおいて，Reasoning word は全て `<reasoning>` で確実に囲まれます．現時点（2025/08/19）ではこちらの方が確実かもしれません．

## 参考リンク

- [OpenAI GPT-OSS](https://github.com/openai/gpt-oss)
