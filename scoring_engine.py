def calculate_score(feedback):

    scores = {
        "Excellent concept understanding.": 95,
        "Good concept understanding.": 80,
        "Average understanding.": 60,
        "Needs Improvement.": 40,
        "Unable to evaluate concept.": 0
    }

    return scores.get(feedback, 0)