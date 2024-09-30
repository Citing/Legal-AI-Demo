from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def chat(prompts):
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompts,
    )
    response = stream.choices[0].message.content

    return response