from rest_framework import serializers

class StudentResult(serializers.Serializer):
    hours_studied = serializers.IntegerField()
    attendance = serializers.IntegerField()