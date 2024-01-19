import os, sys
from openai import OpenAI
from dotenv import load_dotenv

from exception import CustomException

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def make_ai_response(role: str, prompt: str, model: str):
    try:
        ai_response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": role,
                    "content": prompt,
                }
            ],
        )

        return ai_response.choices[0].message.content

    except Exception as e:
        raise CustomException(e, sys)
