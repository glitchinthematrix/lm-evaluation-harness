def doc_to_text(doc) -> str:
    option_choices = {
        "A": doc["ending0"],
        "B": doc["ending1"],
        "C": doc["ending2"],
        "D": doc["ending3"],
    }
    answers = "".join((f"{k}. {v}\n") for k, v in option_choices.items())
    return f"Question: {doc['sent1']}\nOptions:\n{answers}\nPlease only output the choice letter in the answer field e.g. Final Answer: A"


def doc_to_target(doc) -> int:
    return doc["label"] 
