# 💼 Task 5 – Financial Data SQL QA System

### 🧩 Overview
This task demonstrates how to **query structured financial data** using natural language with **LangChain SQLDatabaseChain** and **Google Gemini Pro**.  
Users can ask questions about clients, portfolios, and investments stored in a **SQLite database**, and the system will:

- Generate **SQL queries** automatically from user input  
- Execute the query safely  
- Provide **natural language summaries** of results  

---

### 📂 Folder Contents
```

Task 5 SQL QA System/
├── app.py                 # Streamlit app entry point
├── create_db.py           # Create SQLite database with dummy data
├── db_utils.py            # Ensure DB exists and provide URI
├── qa_chain.py            # LLM chains for SQL generation & summary
├── .env                   # Environment variables (GOOGLE_API_KEY)
└── requirements.txt       # Required Python packages

````

---

### ⚙️ Tech Stack
- **Frontend:** Streamlit  
- **LLM:** Google Gemini Pro (`google-generativeai`)  
- **Framework:** LangChain + SQLDatabaseChain  
- **Database:** SQLite (or easily switch to MySQL/PostgreSQL)  
- **Language:** Python 3.10+  
- **Data Handling:** pandas  

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

3. Ensure `.env` has your Gemini API key:

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

4. Run the Streamlit app:

```bash
cd "Task 5 SQL QA System"
streamlit run app.py
```

5. The system will automatically create a SQLite database `finance.db` with **dummy client and investment data** if not already present.

6. Enter a natural language question, e.g.:

   * "List all clients with portfolio value greater than 300000"
   * "Summarize investments for Client_5"

7. The app displays:

   * **Generated SQL query**
   * **Query result in tabular form**
   * **Natural language summary**

---

### 🧩 Requirements (for standalone use)

If you want to run **only Task 5**:

* **Python version:** 3.10+
* **Dependencies:**

```bash
pip install streamlit pandas langchain langchain_community google-generativeai
```

* **Environment Variables (.env):**

```bash
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

### 💬 Example Interaction

1. Q: "List all clients over 50 years old with high-risk portfolios."

   * Generated SQL: `SELECT * FROM clients WHERE age > 50 AND risk_profile='High';`
   * Summary: "3 clients aged above 50 have high-risk portfolios, including Client_12, Client_19, and Client_27."

2. Q: "What is the total investment in Alpha Growth Fund?"

   * Generated SQL: `SELECT SUM(amount_invested) FROM investments WHERE fund_name='Alpha Growth Fund';`
   * Summary: "The total investment in Alpha Growth Fund is $X, with contributions from multiple clients."
---

### 📸 Screenshots

![alt text](<Screenshot 2025-10-10 172818.png>)
![alt text](<Screenshot 2025-10-10 174801.png>)
![alt text](<Screenshot 2025-10-10 174906.png>)
---

### 🧠 What This Task Demonstrates

* ✅ Natural language → SQL query translation using **Gemini + LangChain**
* ✅ Execution of queries on a **realistic SQLite dataset**
* ✅ Summarization of tabular results into human-readable text
* ✅ Integration of **Streamlit UI** for interactive Q&A

---

### 🪄 Future Enhancements

* Connect to live financial databases (PostgreSQL/MySQL)
* Add user authentication for multi-user datasets
