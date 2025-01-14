import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROP_API_KEY")


from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

model=ChatGroq(model='Gemma2-9b-It',groq_api_key=groq_api_key)

system_message="Translate the folowing into {language}:"
prompt_message=ChatPromptTemplate.from_messages(
    [
        ('system',system_message),
        ('user','{text}')
    ]
)

parser=StrOutputParser()

chain=prompt_message|model|parser

app=FastAPI(title='Langchain Server',
            version='1.0',
            description="A simple API server using Langchain runnable interfaces")

add_routes(app,chain,path='/chain')

if __name__=='__main__':
    import uvicorn
    uvicorn.run(app,host='127.0.0.1',port=8000)


