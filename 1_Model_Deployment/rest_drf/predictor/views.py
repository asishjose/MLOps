from django.shortcuts import render

# Create your views here.
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import PredictionInputSerializer, PredictionOutputSerializer
from .ml.loader import get_model

class PredictView(APIView):
    def post(self, request):
        input_serializer = PredictionInputSerializer(data=request.data)
        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        data = input_serializer.validated_data
        features = np.array([[data['feature1'], data['feature2'], data['feature3']]])

        model = get_model()
        prediction = model.predict(features)[0]

        confidence = None
        if hasattr(model, "predict_proba"):
            confidence = model.predict_proba(features).max()

        output = PredictionOutputSerializer({
            "prediction": prediction,
            "confidence": confidence,
        })
        return Response(output.data, status=status.HTTP_200_OK)
    