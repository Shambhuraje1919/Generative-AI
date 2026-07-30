from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAiEmbeddings(model_name= 'text-3-large', dimension = 32)

documnet = ['whats the capital of maharatsra',
            'whats the capital of goa',
            'what the name of pm of India']
res = embeddings.embed_documents(documnet)

print(str(res))