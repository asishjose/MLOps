from rest_framework import serializers

class IntclsPredict(serializers.Serializer):
    msg_text = serializers.CharField()

class StdclsPredict(serializers.Serializer):
    hrs = serializers.IntegerField()
    att = serializers.IntegerField()