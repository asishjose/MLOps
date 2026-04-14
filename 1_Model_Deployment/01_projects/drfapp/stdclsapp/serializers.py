from rest_framework import serializers

class StdclsPredict(serializers.Serializer):
    hrs = serializers.IntegerField()
    att = serializers.IntegerField()