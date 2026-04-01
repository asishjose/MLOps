from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    BatchPredictionInputSerializer,
    BatchPredictionOutputSerializer,
    PredictionInputSerializer,
    PredictionOutputSerializer,
)
from .ml.loader import get_model


class PredictView(APIView):
    def post(self, request):
        input_serializer = PredictionInputSerializer(data=request.data)
        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        text = input_serializer.validated_data["input"]
        model = get_model()
        prediction = model.predict([text])[0]

        output = PredictionOutputSerializer({
            "input": text,
            "prediction": prediction,
        })
        return Response(output.data, status=status.HTTP_200_OK)


class BatchPredictView(APIView):
    def post(self, request):
        input_serializer = BatchPredictionInputSerializer(data=request.data)
        if not input_serializer.is_valid():
            return Response(input_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        texts = input_serializer.validated_data["inputs"]
        model = get_model()
        predictions = model.predict(texts)

        output = BatchPredictionOutputSerializer({
            "predictions": [
                {"input": text, "prediction": prediction}
                for text, prediction in zip(texts, predictions)
            ]
        })
        return Response(output.data, status=status.HTTP_200_OK)
