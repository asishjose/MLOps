from rest_framework import serializers

class PredictionInputSerializer(serializers.Serializer):
    input = serializers.CharField()
    
