# 🧠 Task 4 – RAG with Memory & Multi-Turn Document QA

### 🧩 Overview
This task is part of the **ManuWorks AI Suite** and extends the basic RAG system (Task 3) by adding **memory and multi-turn conversational capabilities**.  
Users can ask follow-up questions over PDFs such as SOPs, machine manuals, or ISO standards, and the AI will **remember the context** across multiple turns using **LangChain ConversationBufferMemory** and **MultiQueryRetriever**.  

---

### 📂 Folder Contents
```

Task 4 RAG - Part 2 (Memory + Multi-step Retrieval)/
├── app.py                     # Streamlit app entry point
├── configs/
│   └── settings.yaml          # Configuration for PDF path, index path, model, etc.
├── data/                      # Example PDFs uploaded by user
├── index/                     # FAISS index folder
├── src/
│   ├── config.py              # Load YAML configuration
│   ├── loader.py              # PDF loading and splitting
│   ├── embedder.py            # FAISS index creation/loading
│   ├── memory_qa_system.py    # Memory-augmented RAG pipeline
│   ├── retriever.py           # Vectorstore -> retriever
│   └── utils.py               # Helper functions (e.g., print_result)
├── vectorstore.pkl            # Cached vectorstore
├── .env                       # Environment variables (GENAI_API_KEY)
└── requirements.txt           # Required Python packages

````

---

### ⚙️ Tech Stack
- **Frontend:** Streamlit  
- **LLM:** Google Gemini Pro via `google-generativeai`  
- **Framework:** LangChain + `langchain_community`  
- **Vector Store:** FAISS (`faiss-cpu`)  
- **Embeddings:** `sentence-transformers` (`all-MiniLM-L6-v2`)  
- **PDF Handling:** `pypdf` via LangChain loaders  
- **Memory:** ConversationBufferMemory + MultiQueryRetriever  
- **Language:** Python 3.10+  

---

### 🚀 Setup & Run Instructions
1. Activate your virtual environment:
```bash
# Windows PowerShell
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Edit the configuration `configs/settings.yaml` if needed:

```yaml
pdf_path: "data/SOP_Hazardous_Processes.pdf"
index_path: "index/sop_faiss_index"
chunk_size: 500
chunk_overlap: 100
retrieval_k: 3
llm_model: "gemini-2.5-flash"
```

4. Run the Streamlit app:

```bash
cd "Task 4 RAG - Part 2 (Memory + Multi-step Retrieval)"
streamlit run app.py
```

5. Upload a PDF using the sidebar.
6. Ask questions in the input field. The system supports **multi-turn queries** and shows:

   * Generated answer
   * Expandable source documents
   * Conversation history

⚡ **Note:** The first run may take longer for PDF indexing. Subsequent queries are faster.

---

### 🧩 Requirements (for standalone use)

If you want to run **only Task 4**:

* **Python version:** 3.10+
* **Dependencies:**

```bash
pip install streamlit langchain langchain_community faiss-cpu sentence-transformers transformers pypdf pyyaml google-generativeai tqdm
```

* **Environment Variables (.env):**

```bash
GENAI_API_KEY=your_gemini_api_key_here
```

---

### 💬 Example Interaction

* Q1: "List the safety steps for the hydraulic press."
* Q2: "Compare these steps with the CNC lathe."

📄 *Refer to the included PDF file for example Q&A interactions.*

---

### 📸 Screenshots

![alt text](<Screenshot 2025-10-11 012252.png>)
![alt text](<Screenshot 2025-10-11 013842.png>)

---

### 🧠 What This Task Demonstrates

* ✅ Memory-augmented RAG for **multi-turn conversation**
* ✅ Context-aware answers across follow-up queries
* ✅ MultiQueryRetriever for better recall of document context
* ✅ FAISS vectorstore caching for speed
* ✅ Streamlit UI with **conversation history** and **source references**

---

### 🪄 Future Enhancements

* Support multiple PDFs simultaneously
* Integrate hierarchical document retrievers
* Add summarization of previous conversation context
