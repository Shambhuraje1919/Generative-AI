from langchain.openai import OpenAi
from dotenv import load_dotenv

load_dotenv()

LLM = OpenAi(
    model_name="gpt-4o",
    temperature=0.7,
    max_tokens=10,)

result = LLM.invoke("What is the capital of France?")
print(result.content)