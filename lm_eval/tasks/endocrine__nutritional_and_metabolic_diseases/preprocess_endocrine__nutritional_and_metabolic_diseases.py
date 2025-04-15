
def doc_to_text(doc):
    return f"Question: {doc['question']}\n Options:\n{doc['options']}"

def doc_to_target(doc):
    return doc['answer']
