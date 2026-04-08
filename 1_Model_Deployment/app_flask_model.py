from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load  model
model = joblib.load('1_Model_Deployment/intent_classifier.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['input']])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)

