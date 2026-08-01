from langchain_core.runnables import RunnableSequence
from groq_api import model 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


parser = StrOutputParser()

prompt1 = PromptTemplate(
    template= ' tell me the 5 questions on  {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template= ' now give me ans of this quize{que}',
    input_variables= ['que']
)



chain = RunnableSequence(prompt1 , model , parser , prompt2 , model , parser)

print(chain.invoke({'topic': 'narendra modi '}))
