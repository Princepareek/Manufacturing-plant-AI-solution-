import streamlit as st
from core.loader import load_document
from core.splitter import split_documents
from core.summarizer import summarize_documents
from core.utils import save_summary

st.set_page_config(page_title="Summarization Engine", layout="wide")

st.title("📄 Document Summarization Engine")
st.write("Upload a PDF or text file to generate a concise summary using Gemini + LangChain.")

uploaded_file = st.file_uploader("Upload document", type=["pdf", "txt", "docx"])

if uploaded_file:
    file_path = f"data/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ File uploaded successfully!")

    if st.button("Summarize"):
        with st.spinner("Summarizing... please wait ⏳"):
            st.spinner("Loading document...")
            docs = load_document(file_path)
            st.spinner(f"Loaded {len(docs)} document(s).")
            chunks = split_documents(docs)
            st.spinner(f"Split into {len(chunks)} chunks.")
            summary = summarize_documents(chunks)
            st.spinner("Summarization complete!")
            save_path = save_summary(summary)
            st.spinner(f"Summary saved to {save_path}")
            
        st.subheader("🧩 Summary:")
        st.write(summary)
        
        st.download_button("Download Summary", summary, file_name="summary.txt")
        st.info(f"Summary saved at: {save_path}")
