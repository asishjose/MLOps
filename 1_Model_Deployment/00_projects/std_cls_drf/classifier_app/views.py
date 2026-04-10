from django.shortcuts import render

# Create your views here.
import joblib
import os
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PredictSerializer

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'classifier.pkl')
model = joblib.load(MODEL_PATH)

class PredictView(APIView):
    def post(self, request):
        serializer = PredictSerializer(data = request.data)
        if serializer.is_valid():
            attendance = serializer.validated_data['att']
            hours_studied = serializer.validated_data['hrs']
            prediction = model.predict([[hours_studied, attendance]])

            return Response({
                'output':prediction
            })