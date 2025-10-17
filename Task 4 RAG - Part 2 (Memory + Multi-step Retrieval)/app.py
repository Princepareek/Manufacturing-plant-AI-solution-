import streamlit as st
import pickle
import os
from pathlib import Path

from src.config import load_config
from src.loader import load_and_split
from src.embedder import create_or_load_index
from src.memory_qa_system import build_memory_qa_chain


# ----------------------
# Streamlit Page Config
# ----------------------
st.set_page_config(
    page_title="🧠 Conversational RAG with Memory",
    page_icon="🧠",
    layout="wide",
)

st.markdown(
    """
    <style>
    /* Main title style */
    .main-title {
        text-align: center;
        font-size: 2.2em;
        font-weight: 700;
        color: #3b82f6;
    }
    .sub-text {
        text-align: center;
        font-size: 1.1em;
        color: #666;
        margin-bottom: 1.5rem;
    }
    .stTextInput > div > div > input {
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="main-title">🧠 RAG - Conversational Document QA</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-text">Upload your PDF and ask multi-turn questions using Google Gemini Pro!</p>', unsafe_allow_html=True)


# ----------------------
# Load Config
# ----------------------
config = load_config("configs/settings.yaml")
VECTORSTORE_PATH = "vectorstore.pkl"
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)


# ----------------------
# Initialize Session State
# ----------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "doc_processed" not in st.session_state:
    st.session_state.doc_processed = False

if "uploaded_filename" not in st.session_state:
    st.session_state.uploaded_filename = None


# ----------------------
# Sidebar - File Upload
# ----------------------
st.sidebar.header("📂 Document Upload")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])

# Reset if a new file is uploaded
if uploaded_file and uploaded_file.name != st.session_state.uploaded_filename:
    st.session_state.doc_processed = False
    st.session_state.chat_history = []
    st.session_state.uploaded_filename = uploaded_file.name

# ----------------------
# Step 1: Process and Index PDF
# ----------------------
if uploaded_file and not st.session_state.doc_processed:
    pdf_save_path = DATA_DIR / uploaded_file.name

    # Save file locally
    with open(pdf_save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.sidebar.success(f"✅ Uploaded: {uploaded_file.name}")

    # Process & embed
    with st.spinner("🔎 Processing and indexing your document..."):
        docs = load_and_split(str(pdf_save_path), config["chunk_size"], config["chunk_overlap"])
        vectorstore = create_or_load_index(docs, config["index_path"])

        # Save vectorstore
        with open(VECTORSTORE_PATH, "wb") as f:
            pickle.dump(vectorstore, f)

    st.success("✅ Document processed successfully! You can now start asking questions.")
    st.session_state.doc_processed = True


# ----------------------
# Step 2: Load Prebuilt Vectorstore
# ----------------------
if st.session_state.doc_processed:
    if not os.path.exists(VECTORSTORE_PATH):
        st.error("❌ Vectorstore not found! Please re-upload your document.")
        st.stop()

    with open(VECTORSTORE_PATH, "rb") as f:
        vectorstore = pickle.load(f)

    # Build QA Chain
    qa_chain = build_memory_qa_chain(vectorstore, config["llm_model"], config["retrieval_k"])

    # Fix: specify memory output key
    if hasattr(qa_chain, "memory"):
        qa_chain.memory.output_key = "answer"

    # ----------------------
    # Step 3: Chat Interface
    # ----------------------
    st.subheader("💬 Ask Your Questions")
    query = st.text_input("Type your question here...")

    if query:
        with st.spinner("🤔 Thinking..."):
            result = qa_chain({"question": query, "chat_history": st.session_state.chat_history})

        # Save chat history
        st.session_state.chat_history.append((query, result["answer"]))

        # --- Display Answer ---
        with st.container():
            st.markdown("### ✅ Answer")
            st.info(result["answer"])

        # --- Display Sources ---
        with st.expander("📚 View Source Documents"):
            for i, doc in enumerate(result["source_documents"], start=1):
                st.markdown(f"**Source {i}:** {doc.metadata.get('source', 'Unknown')}")
                st.write(doc.page_content[:400] + "...")

    # --- Display Conversation History ---
    if st.session_state.chat_history:
        st.markdown("---")
        st.markdown("### 🧠 Conversation History")
        for idx, (q, a) in enumerate(reversed(st.session_state.chat_history), start=1):
            with st.container():
                st.markdown(f"**Q{idx}:** {q}")
                st.markdown(f"**A{idx}:** {a}")
                st.markdown("---")

else:
    st.info("⬆️ Upload a PDF file from the sidebar to get started.")
