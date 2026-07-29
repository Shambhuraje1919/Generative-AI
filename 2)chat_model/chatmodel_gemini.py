from langchain.gemini import ChatGemini
from dotenv import Load_dotenv

Load_dotenv()

Chat_model = ChatGemini(
    model_name="gemini-1.5-turbo",
    temperature=0.7,    
    max_tokens=10,
)

res = Chat_model.invoke("What is the capital of France?")
print(res.content)