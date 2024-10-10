from dotenv import load_dotenv
import os

load_dotenv()

class APIKey:
    @staticmethod
    def get_key():
        return os.getenv('OPENAI_API_KEY')