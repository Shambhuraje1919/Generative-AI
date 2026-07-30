from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model_name = 'text-embedding-3-large', dimension = 32)

res = embedding.embed_query("whats the capital of maharashtra??")

print(str(res))