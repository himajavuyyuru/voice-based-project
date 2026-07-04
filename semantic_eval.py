def evaluate_concept(transcript):

    if transcript == "Speech could not be recognized.":
        return "Unable to evaluate concept."

    words = len(transcript.split())

    if words > 100:
        return "Excellent concept understanding."

    elif words > 50:
        return "Good concept understanding."

    elif words > 20:
        return "Average understanding."

    else:
        return "Needs Improvement."