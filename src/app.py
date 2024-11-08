from flask import Flask, request, jsonify
from symptom_checker import symptom_checker
from summarizer import summarize_medical_text
from scheduler import schedule_appointment
from classifier import classify_query
from voice_command import recognize_voice_command

app = Flask(__name__)

@app.route('/symptom_check', methods=['POST'])
def symptom_check():
    data = request.json
    question = data.get('question')
    answer = symptom_checker(question)
    return jsonify({'answer': answer})

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text')
    summary = summarize_medical_text(text)
    return jsonify({'summary': summary})

@app.route('/schedule', methods=['POST'])
def schedule():
    data = request.json
    patient_info = data.get('patient_info')
    response = schedule_appointment(patient_info)
    return jsonify({'response': response})

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    query = data.get('query')
    category = classify_query(query)
    return jsonify({'category': category})

@app.route('/voice_command', methods=['GET'])
def voice_command():
    command = recognize_voice_command()
    return jsonify({'command': command})

if __name__ == '__main__':
    app.run(debug=True)
