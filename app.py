import os
from dotenv import load_dotenv

from langchain_ollama import OllamaLLM
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")

prompt = ChatPromptTemplate.from_messages(
  [
    ('system','You are a helpful assistant . Please respond to the question asked'),
    ('user','Question:{question}')
  ]
)

st.title("Simple GenAI App with Gemma Model")
input_text = st.text_input("What question you have in mind?")

llm=OllamaLLM(model='gemma3:1b')
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
  st.write(chain.invoke({"question":input_text}))