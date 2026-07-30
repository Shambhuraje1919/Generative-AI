from langchain.openai import ChatOpenAI
from dotenv import Load_dotenv

Load_dotenv()

Chat_model = ChatOpenAi(
    model_name="gpt-4o",
    temperature=0.7,
    max_tokens=10,)
res = Chat_model.invoke("What is the capital of France?")
print(res.content)