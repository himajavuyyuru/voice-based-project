def generate_report(transcript, feedback, score):

    report = f"""
Voice Based Concept Understanding Analyzer

--------------------------------------------

Transcript

{transcript}

--------------------------------------------

Evaluation

{feedback}

--------------------------------------------

Score

{score}/100

--------------------------------------------

Generated Successfully
"""

    return report