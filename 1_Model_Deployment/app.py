from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load  model
model = joblib.load('intent_classifier.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    prediction = model.predict([data['input']])
    return jsonify({'prediction': prediction[0]})

#if __name__ == '__main__':
    app.run(debug=True)


def detect_intent(message):
    return model.predict([message])[0]

if __name__ == "__main__":
    print(detect_intent("hello"))