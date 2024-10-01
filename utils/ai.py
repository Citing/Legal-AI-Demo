from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def chat(prompts):
    responses = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=prompts,
    )
    response = responses.choices[0].message.content

    return response

def textEmbedding(text):
    responses = client.embeddings.create(
        model="text-embedding-3-large",
        input=text,
        encoding_format="float"
    )
    embedding = responses.data[0].embedding
    return embedding