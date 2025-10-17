# 📄 Task 6 – Document Summarization Engine (Gemini + LangChain)

### 🧩 Overview
This task implements a **document summarization engine** that allows users to upload **PDF, TXT, or DOCX files** and generate concise summaries using **Google Gemini Pro** models.  
The system uses **LangChain** for document processing and chunking, and provides a **Streamlit UI** for interactive use.

---

### 📂 Folder Contents
```

Task 6 Summarization Engine/
├── app.py                     # Streamlit app entry point
├── core/
│   ├── loader.py              # Load PDF, TXT, DOCX files
│   ├── splitter.py            # Chunk documents for processing
│   ├── summarizer.py          # Summarize documents using Gemini Pro
│   └── utils.py               # Save summary to file
├── data/                      # Folder for uploaded files
├── outputs/                   # Saved summaries (created at runtime)
├── config/
│   └── settings.py            # Configuration (API key, chunk size, chain type)
├── .env                       # Environment variables (GEMINI_API_KEY)
└── requirements.txt           # Required Python packages

````

---

### ⚙️ Tech Stack
- **Frontend:** Streamlit  
- **LLM:** Google Gemini Pro (`google-generativeai`)  
- **Framework:** LangChain (document loaders, text splitters, summarization chains)  
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

3. Add your Gemini API key in `.env`:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

4. Run the Streamlit app:

```bash
cd "Task 6 Summarization Engine"
streamlit run app.py
```

5. Upload a PDF, TXT, or DOCX file via the sidebar or main panel.

6. Click **Summarize**. The system will:

   * Load the document
   * Split it into manageable chunks
   * Summarize it using Gemini Pro
   * Display the summary
   * Save the summary to `outputs/summaries`

7. Optionally, download the summary as a text file.

---

### 🧩 Requirements (for standalone use)

To run **only Task 6**:

* **Python version:** 3.10+
* **Dependencies:**

```bash
pip install streamlit langchain langchain_google_genai python-docx pyyaml
```

* **Environment Variables (.env):**

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

---

### 💬 Example Interaction

1. Upload `SOP_Hazardous_Processes.pdf`.
2. Click **Summarize**.
3. Output:

```
The document outlines hazardous processes in the factory. Key safety measures include...
```

4. Summary saved at: `outputs/summaries/summary_20251011_145312.txt`

---

### 📸 Screenshots
![alt text](<Screenshot 2025-10-11 112556.png>)
---

### 🧠 What This Task Demonstrates

* ✅ Multi-format document loading (PDF, TXT, DOCX)
* ✅ Document chunking for large text processing
* ✅ Summarization using **Google Gemini Pro**
* ✅ Interactive **Streamlit UI** with downloadable results

---

### 🪄 Future Enhancements

* Support batch uploads and multi-document summarization
* Add language detection and multilingual summarization
* Integrate with **RAG pipeline** for answering questions from summarized documents
