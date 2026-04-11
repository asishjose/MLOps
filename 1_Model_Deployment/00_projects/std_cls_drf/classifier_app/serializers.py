from rest_framework import serializers

class PredictSerializer(serializers.Serializer):
    att = serializers.IntegerField()
    hrs = serializers.IntegerField()