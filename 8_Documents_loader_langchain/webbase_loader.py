from langchain_community.document_loaders import WebBaseLoader
from dotenv import load_dotenv
from groq_api import model 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate(
    template='answer the following question {question} on the following {webpage}',
    input_variables= ['question', ' webpage']
)
Url = 'https://dailysanchar.in/news/fake-liquor-factory-busted-in-solapur-excise-department-seizes-goods-worth-2-crore/w'

loader = WebBaseLoader(Url)

web_page = loader.load()

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({'question': 'What the headline here and sumammarize this' ,
                   'webpage': web_page[0].page_content})

print(res)
