import streamlit as st
from transformers import pipeline

# Load LLM pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# UI with Streamlit
st.title("AI FAQ Assistant")
question = st.text_input("Ask me a question:")
context = "Artificial Intelligence is transforming various industries by enabling automation and enhancing efficiency."

if st.button("Get Answer"):
    result = qa_pipeline(question=question, context=context)
    st.write("Answer:", result['answer'])
