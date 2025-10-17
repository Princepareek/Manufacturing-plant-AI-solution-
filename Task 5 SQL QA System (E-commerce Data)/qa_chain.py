import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain
from db_utils import get_db_uri

def init_qa_chain():
    """
    Initializes:
    - SQL generation chain (sql_chain)
    - Separate LLM for natural language summaries (summary_llm)
    """
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("Missing GOOGLE_API_KEY in .env file")

    # LLM for SQL generation
    llm_sql = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)
    db = SQLDatabase.from_uri(get_db_uri())
    sql_chain = create_sql_query_chain(llm_sql, db)

    # Separate LLM for summarization
    summary_llm = ChatGoogleGenerativeAI(model="gemini-2.5-pro", temperature=0)

    return sql_chain, summary_llm
