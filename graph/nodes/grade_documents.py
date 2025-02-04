from typing import Any, Dict
from graph.chains.retrieval_grader import retrieval_grader
from graph.state import GraphState

def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search.

    Args:
        state (dict): The current state of the graph
    Returns:
        state (dict): Filtered out irrelevant documents and updated web search state
    """
    print("---Check document relevant yo question---")
    question = state["question"]
    documents = state["documents"]

    filtered_docs = []
    web_search = False
    for d in documents:
        score = retrieval_grader.invoke({"question":question, "document":d.page_content})
        grade = score.binary_score
        if grade.lower()=='yes':
            print("Grade:Document Relevant")
            filtered_docs.append(d)
        else:
            print("Grade:Document Not Relevant")
            web_search = True
            continue

    return {"question":question, "documents":filtered_docs, "web_search":web_search}