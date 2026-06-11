import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain.chat_models import init_chat_model
from prompts import category_prompt, priority_prompt, routing_prompt, response_prompt

# Initialize deterministic model via Groq 
llm = init_chat_model(
    model="llama-3.1-8b-instant", 
    model_provider="groq", 
    temperature=0
)
str_parser = StrOutputParser()

# Establish sub-chains
category_chain = category_prompt | llm | str_parser
priority_chain = priority_prompt | llm | str_parser
routing_chain  = routing_prompt  | llm | str_parser
response_chain = response_prompt | llm | str_parser

# Concurrency orchestration mapping
map_chain = RunnableParallel(
    category=category_chain,
    priority=priority_chain,
    routing_queue=routing_chain,
    response_draft=response_chain
)