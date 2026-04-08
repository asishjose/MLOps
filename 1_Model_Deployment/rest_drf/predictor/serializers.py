from rest_framework import serializers


class PredictionInputSerializer(serializers.Serializer):
    input = serializers.CharField()


class PredictionOutputSerializer(serializers.Serializer):
    input = serializers.CharField()
    prediction = serializers.CharField()


class BatchPredictionInputSerializer(serializers.Serializer):
    inputs = serializers.ListField(
        child=serializers.CharField(),
        allow_empty=False,
    )


class BatchPredictionItemSerializer(serializers.Serializer):
    input = serializers.CharField()
    prediction = serializers.CharField()


class BatchPredictionOutputSerializer(serializers.Serializer):
    predictions = BatchPredictionItemSerializer(many=True)
