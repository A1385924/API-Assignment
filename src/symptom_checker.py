from transformers import pipeline

def symptom_checker(question):
    model = pipeline('question-answering', model='deepset/roberta-base-squad2')
    context = "Your medical context here"
    result = model(question=question, context=context)
    return result['answer']
