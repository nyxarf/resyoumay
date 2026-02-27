from openai import OpenAI
import os

client = OpenAI(
    api_key="api key here",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Tell me a joke"}
    ]
)

print(response.choices[0].message.content)