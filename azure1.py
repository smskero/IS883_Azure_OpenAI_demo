# azure.py
# Import necessary libraries
import streamlit as st
import openai
import os
# azure.py
# Import necessary libraries
import streamlit as st
#import nltk
#nltk.download('punkt')
import tiktoken


# Replace these imports with your actual backend code
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# Set up your OpenAI API key
openai_api_key = os.environ.get('OPENAI_API_KEY')

# Initialize Streamlit
st.title("Boston City Code Chatbot")
st.subheader("Welcome to the Boston City Code Chatbot! Your one stop shop for all things Boston law.")

uploaded_file = st.file_uploader('Short Boston Code.pdf')
if uploaded_file is not None:
    text = uploaded_file.read()

# Create a text input field for user queries
user_input = st.text_input("Please input your question below:")

# Your backend code starts here

if user_input:
    # Your existing backend code
    query = user_input  # Assuming the user input is the query
    
    # Replace this block with your existing backend code
    dataset_corpus_path = "Short Boston Code.pdf"
    
    pdf_loader = PyPDFDirectoryLoader(dataset_corpus_path)
    documents = pdf_loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=750,
        chunk_overlap=100
    )
    
    chunks = pdf_loader.load_and_split(text_splitter)
    
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key, temperature = 0.3)
    db = FAISS.from_documents(chunks, embeddings)
    
    chain = load_qa_chain(OpenAI(openai_api_key=openai_api_key), chain_type="stuff")
    
    docs = db.similarity_search(query, k=2)
    
    result = chain.run(input_documents=docs, question=query)
    
    # Display the result
    st.write(result)  # Modify this to display the result as needed
