# GPT4LangBridge 🌐

A simple and efficient language translator built using Azure OpenAI GPT-4 (Foundry).  
This proof-of-concept shows how to connect to your Azure deployment and use GPT-4 to translate text into any language using chat-style prompts.

## 🚀 Features
- Powered by GPT-4 via Azure OpenAI
- Supports dynamic target languages
- Simple Python CLI (can be extended to web or API)

## 🧠 Tech Stack
- Python 3
- OpenAI SDK (v1+)
- Azure OpenAI (Foundry Deployment)

## 📦 How to Run

1. Install dependencies:
```bash
pip install openai

2. Set environment variable or update script:
   export AZURE_OPENAI_KEY="your-api-key"

3. Run the script:
   python3 translate.py

✅ Example
Input: "How are you today?"
Target Language: Spanish
Output: "¿Cómo estás hoy?"
