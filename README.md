 Medical Chatbot (Symptom-Based Disease Predictor)

# About the Project..
This project is a simple medical chatbot developed using Python and Flask.  
It predicts possible diseases based on user symptoms and suggests basic medicines.

The chatbot provides quick responses using a dataset of diseases, symptoms, and medicines.

 Note: This project is for educational purposes only and should not be used for real medical diagnosis.

# Features...
- Chatbot-style user interface   
- Symptom-based disease prediction  
- Medicine suggestions  
- Simple and clean UI  
- Fast response using CSV datasets  

# Technologies Used
- Python  
- Flask  
- HTML  
- CSS  
- JavaScript  
- Pandas  


#  Project Structure
medical_chatbot/ │ ├── app.py ├── symptoms.csv ├── medicine_dataset.csv │ ├── templates/ │     └── index.html │ ├── static/ │     └── style.css │ └── README.md

# How to Run the Project

1. Install required libraries:
pip install flask pandas

2. Run the application:
python app.py
  
3. Open browser and go to:
http://127.0.0.1:5000⁠

# How It Works

1. User enters symptoms (e.g. fever, cough)  
2. Backend processes input  
3. Matches symptoms with dataset  
4. Predicts disease  
5. Displays suggested medicine  

# Example

Input:
fever,cough

Output:
Disease: Flu
Medicine: Paracetamol


# Disclaimer
This chatbot is not a substitute for professional medical advice.  
Always consult a doctor for proper diagnosis and treatment

# Author
Laxmi S
