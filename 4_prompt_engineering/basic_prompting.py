from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace
from model import model



prompt = 'whats the capital of china'
res = model.invoke(prompt)
print(res.content)
