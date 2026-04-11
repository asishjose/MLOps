from django.shortcuts import render

# Create your views here.
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentResult

class PredictView(APIView):
    def post(self, request):
        serializer = StudentResult(data=request.data)

        if serializer.is_valid():
            response = requests.post(
                "http://classifier:5000/predict",
                json = serializer.validated_data
            )
            return Response(response.json())
        
        return Response(serializer.errors, status=400)
    



    #### Exceptions and Errors Handled

    # class PredictView(APIView):
    # def post(self, request):
    #     serializer = StudentResult(data=request.data)

    #     if serializer.is_valid():
    #         payload = serializer.validated_data

    #         print("Payload:", payload)

    #         try:
    #             response = requests.post(
    #                 "http://127.0.0.1:5000/predict",
    #                 json=payload,
    #                 timeout=5
    #             )

    #             if response.status_code == 200:
    #                 result = response.json()

    #                 return Response({
    #                     "prediction": result,
    #                     "status": "success"
    #                 })

    #             return Response({
    #                 "error": "ML service failed",
    #                 "details": response.text
    #             }, status=500)

    #         except Exception as e:
    #             return Response({"error": str(e)}, status=500)

    #     return Response(serializer.errors, status=400)