def doc_to_text(doc) -> str:
    option_choices = {
        "A": doc["options"][0],
        "B": doc["options"][1],
        "C": doc["options"][2],
        "D": doc["options"][3],
    }
    answers = "".join((f"{k}. {v}\n") for k, v in option_choices.items())
    return f"Question: {doc['centerpiece']}\nOptions:\n{answers}"


def doc_to_target(doc) -> int:
    return doc["correct_options"]
