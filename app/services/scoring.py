def calculate_scores(questions, answers):
    scores = {}

    for q in questions:
        scale = q["scale"]
        value = answers.get(q["id"], 0)

        scores.setdefault(scale, 0)
        scores[scale] += value

    return scores
