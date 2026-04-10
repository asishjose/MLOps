from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load model once (same as DRF logic)
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'intent_classifier.pkl')
model = joblib.load(MODEL_PATH)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Validation (like serializer in DRF)
        if not data or 'text' not in data:
            return jsonify({
                "error": "Missing 'text' field"
            }), 400

        text = data['text']

        # Prediction
        prediction = model.predict([text])

        return jsonify({
            "input": text,
            "prediction": prediction[0]
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == '__main__':
    app.run(debug=True)