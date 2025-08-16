import streamlit as st
from utils import ocr, table_extraction, rag

st.title("Visual Document RAG System")

uploaded_file = st.file_uploader("Upload PDF or Image", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file:
    st.write("Processing...")
    text, tables, charts = ocr.process_document(uploaded_file)
    st.write("Extracted Text:", text[:500])
    st.write("Tables:", tables)
    st.write("Charts detected:", charts)
    
    query = st.text_input("Ask a question:")
    if query:
        results = rag.query_text(query)
        st.write(results)
