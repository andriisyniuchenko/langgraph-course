import os
from dotenv import load_dotenv

from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langsmith import Client

load_dotenv()

LLM_MODEL = os.getenv("LLM_MODEL")

llm = ChatGroq(model=LLM_MODEL, temperature=0)


prompt = Client().pull_prompt("rlm/rag-prompt", dangerously_pull_public_prompt=True)

generation_chain = prompt | llm | StrOutputParser()