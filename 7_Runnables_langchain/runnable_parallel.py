from typing import Sequence
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableParallel,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from config.groq_api import model
from langchain_core.tracers import Run

prompt1 = PromptTemplate(
    template= ' Generate 3 line twitter post on {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate (
    template= ' generate a linkdin post , regards i have masterd this skills  on{topic}',
    input_variables= ['topic']
)

prompt3 = PromptTemplate(
    template= "summarize the {tweet}",
    input_variables= ['tweet']
)
parser = StrOutputParser()

parallel_chain= RunnableParallel({
   "tweets": RunnableSequence(prompt1 , model ,parser ),
   "linkdin": RunnableSequence(prompt2, model , parser,
                               RunnableLambda(lambda tweet: {"tweet": tweet}),
                                 prompt3 , model , parser),
})

res = parallel_chain.invoke({"topic" : "AI"})
print(res['tweets'])
print(res["linkdin"])
print(res)


parallel_chain.get_graph().print_ascii()