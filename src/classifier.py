from transformers import pipeline

def classify_query(query):
    classifier = pipeline('zero-shot-classification', model='facebook/bart-large-mnli')
    labels = ["symptom", "appointment", "general inquiry"]
    result = classifier(query, candidate_labels=labels)
    return result['labels'][0]
