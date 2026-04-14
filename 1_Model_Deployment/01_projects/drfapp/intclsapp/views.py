from django.shortcuts import render
import os
import joblib

# Create your views here.
from .serializers import IntclsPredict, StdclsPredict
import requests
from rest_framework.response import Response
from rest_framework.views import APIView


MODEL_PATH_INT = os.path.join(os.path.dirname(__file__), 'intent_classifier.pkl')
int_cls_model = joblib.load(MODEL_PATH_INT)

class IntclsPredictView(APIView):
    def post(self, request):
        serializer = IntclsPredict(data=request.data)

        if serializer.is_valid():
            text = serializer.validated_data['msg_text']
            int_response = int_cls_model.predict([text])

            return Response({"prediction": int_response[0]})
        
        return Response(serializer.errors, status=400)
    

MODEL_PATH_STD = os.path.join(os.path.dirname(__file__), 'classifier.pkl')
std_res_model = joblib.load(MODEL_PATH_STD)

class StdclsPredictView(APIView):
    def post(self, request):
        serializer = StdclsPredict(data=request.data)

        if serializer.is_valid():
            hrs = serializer.validated_data['hrs']
            att = serializer.validated_data['att']
            res_response = std_res_model.predict([[hrs, att]])

            return Response({'Result': res_response})
        return Response(serializer.errors, status=400)