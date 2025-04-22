
# from langchain_openai import ChatOpenAI

from langchain_community.chat_models import ChatOpenAI

from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st

import os

from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRAINING_V2"]="true"

##prompt template

prompt=ChatPromptTemplate.from_messages(
[

    ("system","You are a helpful assistant. Please respond to the user queries"),
    ("user","Question:{question}")
]

)

##streamlit framework

st.title("Langchain demo with openai api")
input_text=st.text_area("Enter your question here")

#openai llm

# llm=ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model_name="gpt-3.5-turbo")


output_parser=StrOutputParser()
chain=prompt |llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
    # output=chain.run({"question":input_text})
    # st.write(output)
