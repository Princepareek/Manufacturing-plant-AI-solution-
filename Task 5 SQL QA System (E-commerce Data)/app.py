import streamlit as st
import sqlite3
import pandas as pd
import re
from qa_chain import init_qa_chain
from db_utils import get_db_uri

st.set_page_config(page_title="💼 SQL QA System", layout="wide")
st.title("💬 Financial Data SQL QA System (Gemini + LangChain + SQLite)")

# Initialize chains
try:
    sql_chain, summary_llm = init_qa_chain()
    db_path = get_db_uri().replace("sqlite:///", "")
    st.success("✅ Connected to Database and Gemini API successfully.")
except Exception as e:
    st.error(f"Initialization Error: {e}")
    st.stop()

st.markdown("### 💡 Ask a question about your financial data:")
user_query = st.text_input(
    "Example: 'List all clients with portfolio value greater than 300000'"
)

if st.button("Run Query") and user_query.strip():
    with st.spinner("💭 Thinking..."):
        try:
            # 1️⃣ Generate SQL
            llm_output = sql_chain.invoke({"question": user_query})

            # 2️⃣ Extract only SQL portion
            match = re.search(r"SQLQuery:\s*(.*)", llm_output, flags=re.IGNORECASE | re.DOTALL)
            if match:
                sql_query = match.group(1).strip()
            else:
                sql_query = llm_output.strip()

            # 3️⃣ Remove LIMIT if LLM added one
            sql_query = re.sub(r"limit \d+", "", sql_query, flags=re.IGNORECASE).strip()

            st.markdown("**Generated SQL:**")
            st.code(sql_query, language="sql")

            # 4️⃣ Execute SQL safely
            conn = sqlite3.connect(db_path)
            df = pd.read_sql_query(sql_query, conn)
            conn.close()

            # 5️⃣ Convert results to CSV for LLM summary
            data_str = df.to_csv(index=False)

            # 6️⃣ Generate natural language summary
            summary_prompt = f"""
Here is the result of your query:

{data_str}

Please summarize this data in plain English in 2-3 sentences.
Include the names of clients in the summary if the list is shorter than 20.
Otherwise, provide aggregate info and notable examples.
"""
            nl_summary = summary_llm.predict(summary_prompt)

            st.markdown("**Natural Language Summary:**")
            st.write(nl_summary)

        except Exception as e:
            st.error(f"❌ Error: {e}")
else:
    st.warning("Please enter a question first.")
