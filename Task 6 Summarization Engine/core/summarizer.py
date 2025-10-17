from langchain.chains.summarize import load_summarize_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import GEMINI_API_KEY, DEFAULT_CHAIN_TYPE

def summarize_documents(docs, chain_type=DEFAULT_CHAIN_TYPE):
    if not docs:
        raise ValueError("No documents provided for summarization.")

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=GEMINI_API_KEY)
    chain = load_summarize_chain(llm, chain_type=chain_type)
    summary = chain.run(docs)

    return summary
