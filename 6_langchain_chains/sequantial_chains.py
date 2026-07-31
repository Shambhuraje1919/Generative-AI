from langchain_core.prompts import PromptTemplate
from model import model
from  langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template = "Generate a report on this {topic}",
    input_variables = ["topic"]
)

prompt2 = PromptTemplate(
    template = 'Summarize the report in 4 bullet points /n {report}',
    input_variables = ['report']
)

model = model

parser = StrOutputParser()


chain = prompt1 | model | parser | prompt2 | model | parser

res = chain.invoke({'topic': "cat and dog diffences"})

print(res)

chain.get_graph().print_ascii()