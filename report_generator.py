from reportlab.pdfgen import canvas

def generate_pdf(
    filename,
    transcript,
    similarity,
    score,
    classification
):
    """
    Generate PDF report.
    """
    c = canvas.Canvas(filename)

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 800,
                 "Voice Based Concept Understanding Report")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Transcript: {transcript[:80]}")
    c.drawString(50, 720,
                 f"Semantic Similarity: {similarity}")
    c.drawString(50, 690,
                 f"Understanding Score: {score}%")
    c.drawString(50, 660,
                 f"Classification: {classification}")

    c.save()