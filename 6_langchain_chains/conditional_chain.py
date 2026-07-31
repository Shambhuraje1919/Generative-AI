from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import (RunnableBranch,RunnableLambda,RunnablePassthrough,
)
from model import model
from pydantic import BaseModel, Field
from typing import Literal

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )


parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="""
Classify the sentiment of the following feedback into positive or negative.

{feedback}

{format_instruction}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": parser2.get_format_instructions()
    },
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="Write an appropriate response to this positive feedback:\n{feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=["feedback"],
)

chain = (
    RunnablePassthrough.assign(sentiment=classifier_chain)
    | RunnableBranch(
        (
            lambda x: x["sentiment"].sentiment == "positive",
            prompt2 | model | parser,
        ),
        (
            lambda x: x["sentiment"].sentiment == "negative",
            prompt3 | model | parser,
        ),
        RunnableLambda(lambda x: "Could not find sentiment"),
    )
)

print(chain.invoke({"feedback": "This is a beautiful phone"}))

chain.get_graph().print_ascii()