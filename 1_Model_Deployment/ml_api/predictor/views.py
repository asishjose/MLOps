from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(BASE_DIR, "intent_classifier.pkl"))

@api_view(['POST'])
def predict(request):
    text = request.data.get('input')

    if not text:
        return Response({"error": "No input"}, status=400)
    
    prediction = model.predict([text])[0]

    return Response({
        "input":text,
        "prediction": prediction
    })