from django.shortcuts import render

# Create your views here.
import joblib
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictSerializer

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'intent_classifier.pkl')
model = joblib.load(MODEL_PATH)

class PredictView(APIView):
    def post(self, request):
        serializer = PredictSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            prediction = model.predict([text])
            return Response({
                'input': text,
                'ouput': prediction
            })
        



