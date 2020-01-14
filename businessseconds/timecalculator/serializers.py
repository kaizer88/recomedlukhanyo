from rest_framework import serializers

class CalculateTimeSerializer(serializers.Serializer):
    """ Serializer start date and end date field """
    start_date = serializers.DateField()
    end_date = serializers.DateField()


