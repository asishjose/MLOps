from rest_framework import serializers

class ClsPredict(serializers.Serializer):
    hrs = serializers.IntegerField()
    att = serializers.IntegerField()