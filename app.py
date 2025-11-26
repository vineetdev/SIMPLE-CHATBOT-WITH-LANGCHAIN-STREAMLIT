from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
    ("system","You are a helpful assistant. Please response to the user queries accurately and concisely"),
    ("user","Question: {question}")
    ]
)
    
## streamlit app 
st.title("Chatbot Application using Langchain and OpenAI")
user_input = st.text_input("Enter your question:")

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser 

if user_input:
    st.write(chain.invoke({"question": user_input}))
