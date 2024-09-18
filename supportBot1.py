import streamlit as st
from faq import faq
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
from typing import List
from langchain_community.document_loaders import (
    CSVLoader,
    DataFrameLoader,
    PDFMinerLoader,
    TextLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredExcelLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
#from chromadb.config import Settings
#from langchain_community.vectorstores import Chroma
#from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import pandas
import pandas as pd
import tabulate
import glob
import os
st.set_page_config(page_title="OptiAI")
st.markdown(
    r"""
    <style>
    .stDeployButton {
            visibility: hidden;
        }
    </style>
    """, unsafe_allow_html=True
)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#os.environ["OPENAI_API_KEY"] = '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'
os.environ["OPENAI_API_KEY"] = 'sk-PqvoEp2YHEP-bIIna_yK72oPKEJsLhEG9M3rZmrQRbT3BlbkFJ4wu3WS_0OWtriaLOBl1V6b5rndrDc4s95JDDmuVngA'
#DOC_DIRECTORY='./insight'
DOC_DIRECTORY='./files'
def initCSV(msg):
    joined_files = os.path.join(DOC_DIRECTORY, "*.csv")
    joined_list = glob.glob(joined_files)
    df = pd.concat(map(pd.read_csv, joined_list), ignore_index=True)
    agent = create_pandas_dataframe_agent(ChatOpenAI(temperature=0.3, model="gpt-4o-mini"), df, agent_type="openai-tools", verbose=True,allow_dangerous_code=True,handle_parsing_errors=True)
    response = agent.invoke(msg)
    print(response)
    return response
def display_result(prompt):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    res = initCSV(prompt)
    answer = res['output']
    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.chat_message("assistant").write(answer)
def main():
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    #st.image("optiex_robo.png",width=100)
    #st.title("OptiAI")
    #st.caption("Ask me anything!")
    col1,col2 = st.columns([1,4])
    with col1:
        st.image("optiex_robo.png",width=100)
    with col2:
        st.title("OptiAI")
        st.caption("Ask me anything!")
#    st.sidebar.title("")
#    st.sidebar.write('Welcome to the GovGrants AI chatbot, your go-to resource for all inquiries about our product! GovGrants is a comprehensive platform designed to streamline government processes and enhance public service delivery. Whether you have questions about how GovGrants can simplify bureaucratic procedures, improve transparency, or increase citizen engagement, our chatbot is here to assist you. From explaining features and functionalities to providing insights on implementation strategies, we\'re dedicated to ensuring you have a seamless experience with GovGrants. So go ahead, ask us anything about GovGrants, and we\'ll be delighted to assist you!')
#    with st.sidebar:
#        faq()
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])
    if prompt := st.chat_input():
        display_result(prompt)
if __name__ == "__main__":
    main()