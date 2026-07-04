from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load Sentence-BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

def calculate_similarity(reference_text, student_text):
    """
    Calculate semantic similarity.
    """
    embeddings = model.encode([reference_text, student_text])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return round(float(similarity), 4)