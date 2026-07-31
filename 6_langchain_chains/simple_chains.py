from langchain_core.prompts import PromptTemplate
from model import model
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate(
    template= "Generate   interesting story about {topic}",
    input_variables= ["topic"]
)

model = model

parser = StrOutputParser()


chain = prompt | model  | parser

res = chain.invoke({'topic': "AI Killed my job"})

print(res)

chain.get_graph().print_ascii()
