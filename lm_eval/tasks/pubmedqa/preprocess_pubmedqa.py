def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])
    options = '\nA. Yes\nB. No\nC. Maybe'
    return "Abstract: {}\nQuestion: {}\nOptions: {}".format(
        ctxs,
        doc["QUESTION"],
        options,
    )

def doc_to_target(doc) -> int:
    a =  doc["final_decision"] 
    if a == "yes":
        return 0
    elif a == "no":
        return 1
    else:
        return 2
