import os
from dotenv import load_dotenv

load_dotenv()

from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st


## Langsmith Tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")


##Prompt Template setting

prompt=ChatPromptTemplate.from_messages(
    [
        ('system','You Are an AI Assistant,Please Help'),
        ('user','Question:{question}')

    ]
)

##streamlit framework

st.title("GenAI with Ollama3")
input_text=st.text_input("Search for anything")


##Ollama3 model

llm=Ollama(model='llama3')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

