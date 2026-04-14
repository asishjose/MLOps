from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ClsPredict
import os
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), "classifier.pkl")
model = joblib.load(MODEL_PATH)

class StudentResultPredictView(APIView):
    def post(self, request):
        serializer = ClsPredict(data = request.data)

        hrs = serializer.validated_data['hrs']
        att = serializer.validated_data['att']

        result_response = model.predict([['hrs', 'att']])
        return Response(result_response)