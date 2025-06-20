from openai import AzureOpenAI
import os

# Use env variable or paste your key directly here
api_key = os.getenv("AZURE_OPENAI_KEY", "********")

client = AzureOpenAI(
    api_key=api_key,
    api_version="2025-01-01-preview",
    azure_endpoint="https://*****/",
)

def translate_text(text, target_language="French"):
    prompt = f"Translate this into {target_language}:\n\n{text}"

    response = client.chat.completions.create(
        model="gpt-4o",  # Your Azure deployment name
        messages=[
            {"role": "system", "content": "You are a helpful translator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content.strip()

# Example usage
if __name__ == "__main__":
    original = "How are you doing today?"
    translated = translate_text(original, target_language="Hindi")
    print("Translated Text:", translated)

