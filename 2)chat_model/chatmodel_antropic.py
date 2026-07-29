from langchain.anthropic import ChatAnthropic
from dotenv import Load_dotenv

Load_dotenv()   

Chat_model = ChatAnthropic(
    model_name="claude-2",
    temperature=0.7,    
    max_tokens=10,
)
res = Chat_model.invoke("What is the capital of France?")
print(res.content)