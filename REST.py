from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load your model
model = pickle.load(open('heart_disease.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json  # Expecting a JSON payload
    # Convert to DataFrame (Flask sends a dict)
    df = pd.DataFrame([data])
    # Predict
    prediction = int(model.predict(df)[0])
    probability = float(model.predict_proba(df)[0][1])  # % chance of disease
    return jsonify({
        "prediction": prediction, 
        "risk_score": round(probability*100,2)
    })

if __name__ == "__main__":
    app.run(debug=True)
