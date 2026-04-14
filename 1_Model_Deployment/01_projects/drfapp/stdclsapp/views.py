from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StdclsPredict

import os
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'classifier.pkl')
model = joblib.load(MODEL_PATH)

class StdclsPredictView(APIView):
    def post(self, request):
        serializer = StdclsPredict(data=request.data)

        if serializer.is_valid():
            hrs = serializer.validated_data['hrs']
            att = serializer.validated_data['att']
            res_response = model.predict([[hrs, att]])

            return Response({'Result': res_response})
        return Response(serializer.errors, status=400)