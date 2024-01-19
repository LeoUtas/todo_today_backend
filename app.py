import sys, os
from fastapi import FastAPI
from ai_requests import make_ai_response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv

from exception import CustomException


load_dotenv()


class Item(BaseModel):
    percentage_done: float


model = "gpt-3.5-turbo"
personality = "hilarious"
number_of_word = 8
role = "assistant"
note = "do not repeat the sentence, make your message random"


app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
    "https://todotoday0.netlify.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/get-ai-response/")
async def get_ai_response(percentage_done: Item):
    try:
        prompt = (
            f"You are a {personality} assistant,"
            + f" making a {number_of_word}-word sentence"
            + f" to inspire somebody who just got {percentage_done}% of the work done."
            + f"{note}"
        )

        response = make_ai_response(role, prompt, model)

        return {"ai_response": response}
    except Exception as e:
        raise CustomException(e, sys)


# if __name__ == "__main__":
#     import uvicorn

#     port = int(
#         os.environ.get("PORT", 8000)
#     )  # define port so we can map container port to localhost

#     uvicorn.run("app:app", host="0.0.0.0", port=port, reload=True)
