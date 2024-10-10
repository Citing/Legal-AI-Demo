from openai import OpenAI
from utils.apiKey import APIKey

class AIAgent:
    def __init__(self):
        self.client = OpenAI(api_key=APIKey.get_key())

    def chat(self, prompts):
        responses = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=prompts,
        )
        response = responses.choices[0].message.content

        return response

    def textEmbedding(self, text):
        responses = self.client.embeddings.create(
            model="text-embedding-3-small",
            input=text,
            encoding_format="float"
        )
        embedding = responses.data[0].embedding
        return embedding