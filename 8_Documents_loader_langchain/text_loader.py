from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from groq_api import model
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from numpy import dtype


load_dotenv() 


prompt = PromptTemplate(
    template= "Summarize this {doc}",
    input_variables= ['doc']
)

parser = StrOutputParser()


loader = TextLoader(
    "8_Documents_loader_langchain/cricket.txt",
    encoding="utf-8"
)


docs = loader.load()

#print(docs[0].page_content)
print(len(docs))
print(type(docs[0]))
print(docs[0].metadata)


chain = prompt | model | parser

res = chain.invoke({'doc':docs[0].page_content})
print(res)






