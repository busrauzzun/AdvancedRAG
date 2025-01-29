from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field


llm = ChatOpenAI(temperature=0)

class GradeAnswer(BaseModel):

    binary_score:str = Field(
        description="Answer addresses the question, 'yes' or 'no"
    )
structured_llm_grader = llm.with_structured_output(GradeAnswer)

system_prompt = """
You are a grader assessing whether an answer addresses / resolves a question.\n
Give a binary score 'yes' or 'no'. Yes' means that the answer resolves the question.
"""
answer_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "User question: \n\n {question} \n\n LLM generation: {generation}")
    ]
)