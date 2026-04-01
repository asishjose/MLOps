from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    feature1 = serializers.FloatField()
    feature2 = serializers.FloatField()
    feature3 = serializers.FloatField()


class PredictionOutputSerializer(serializers.Serializer):
    prediction = serializers.FloatField()
    confidence = serializers.FloatField(required=False)
    