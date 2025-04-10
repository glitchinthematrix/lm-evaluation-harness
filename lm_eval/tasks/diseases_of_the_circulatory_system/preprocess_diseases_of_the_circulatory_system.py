
def doc_to_text(doc):
    return f"{doc['question']}\n{doc['options']}"

def doc_to_target(doc):
    return doc['answer']
