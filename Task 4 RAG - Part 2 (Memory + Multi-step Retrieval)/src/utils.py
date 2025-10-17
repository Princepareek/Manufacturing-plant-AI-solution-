def print_result(result):
    """
    Nicely print QA result.
    """
    print("\n🔹 Answer:\n", result["answer"])
    print("\n🔹 Sources:")
    for doc in result["source_documents"]:
        print("-", doc.metadata.get("source"), "| Page:", doc.metadata.get("page", "N/A"))
