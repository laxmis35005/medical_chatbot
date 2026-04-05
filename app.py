from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load datasets
symptoms_data = pd.read_csv("symptoms.csv")
medicine_data = pd.read_csv("medicine_dataset.csv")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    user_input = data['symptoms'].lower()
    user_symptoms = [s.strip() for s in user_input.split(',')]

    best_match = None
    max_match = 0


    for index, row in symptoms_data.iterrows():

        dataset_symptoms = [
            str(row['symptom1']).lower(),
            str(row['symptom2']).lower(),
            str(row['symptom3']).lower()
        ]


        match_count = len(set(user_symptoms) & set(dataset_symptoms))

        if match_count > max_match:
            max_match = match_count
            best_match = row['disease']

    if best_match is None:
        return jsonify({
            "disease": "Not Found",
            "medicine": "Please consult a doctor"
        })

    
    med_row = medicine_data[medicine_data['disease'] == best_match]

    if not med_row.empty:
        medicine = med_row.iloc[0]['medicine']
    else:
        medicine = "Consult doctor"

    return jsonify({
        "disease": best_match,
        "medicine": medicine
    })

if __name__ == "__main__":
    app.run(debug=True)