from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.llms.base import LLM
import google.generativeai as genai
import os
from dotenv import load_dotenv


class GeminiLLM(LLM):
    model_name: str
    api_key: str

    @property
    def _llm_type(self):
        return "gemini-2.5-flash"

    def _call(self, prompt, stop=None):
        genai.configure(api_key=self.api_key)
        model = genai.GenerativeModel(self.model_name)
        response = model.generate_content(prompt)
        return getattr(response, "text", "")


def build_memory_qa_chain(vectorstore, model_name="gemini-2.5-flash", k=3):
    """
    Build a conversational RAG pipeline with memory and multi-query retrieval.
    """
    load_dotenv()
    api_key = os.getenv("GENAI_API_KEY")
    if not api_key:
        raise ValueError("GENAI_API_KEY not found in environment variables!")

    llm = GeminiLLM(model_name=model_name, api_key=api_key)

    # Multi-query retriever (expands queries for better recall)
    base_retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    retriever = MultiQueryRetriever.from_llm(retriever=base_retriever, llm=llm)

    # Add conversation memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        verbose=True
    )

    return qa_chain
