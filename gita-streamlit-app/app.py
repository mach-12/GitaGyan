from langchain.vectorstores import FAISS
from langchain import hub
from langchain.chains import RetrievalQA
from langchain.llms import Ollama, OpenAI
import pandas as pd
from langchain.document_loaders import DataFrameLoader
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
import streamlit as st
from langchain.llms import Ollama

st.title("Takshila")

@st.cache_resource
def on_startup():
    st.session_state.messages = []
    return 

@st.cache_resource
def load_vectorstore():
    
    QA_CHAIN_PROMPT = hub.pull("rlm/rag-prompt-llama")
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    PATH_TO_EMBEDDINGS = "gita-embedding"
    db = FAISS.load_local(PATH_TO_EMBEDDINGS, embeddings = embeddings)

    llm = Ollama(base_url='http://localhost:11434',
    model="llama2:13b")

    qa_chain = RetrievalQA.from_chain_type(
        llm,
        retriever=db.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
    )
    return qa_chain

if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({"role": "assistant", "content": f"Jai Shree Krishna. Ask your doubts"})

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

qa_chain = load_vectorstore()

prompt = st.chat_input()

if prompt:
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        st.session_state.messages.append({"role": "user", "content": prompt})
    except:
        st.session_state.messages = []

    with st.chat_message("assistant"):
        BASE_PROMPT = """
        You will always return markdown syntax in this format.
        Format:
        Sanskrit Verse relevant the problem:
        Transliteration:
        Translation:
        Meaning and Explanation:
        
        Please retrieve a relevant verse from the Bhagavad Gita that discusses the concept of duty (Dharma) and its significance. Provide the shloka in Sanskrit, followed by its transliteration, translation, and the deeper meaning behind the verse.
        Always answer in markdown format. 
    """
        
        END_PROMPT = "When asked for a question. give the relevant sanskrit verse or just make conversation"

        message_placeholder = st.empty()
        full_response = qa_chain({"query":BASE_PROMPT +prompt + END_PROMPT})["result"]
        message_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    