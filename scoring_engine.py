def calculate_score(similarity):
    """
    Convert similarity to percentage score.
    """
    return round(similarity * 100, 2)


def classify_understanding(score):
    """
    Classify understanding level.
    """
    if score >= 90:
        return "Excellent"
    elif score >= 75:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"