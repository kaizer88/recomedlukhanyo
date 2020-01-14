
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# import datetime as dt
from datetime import date, timedelta

import holidays

from . import serializers
# Create your views here.

class CalculateTime(APIView):

    serializer_class = serializers.CalculateTimeSerializer
    za_holidays = holidays.SouthAfrica()

    def post(self, request):

        serializer =  self.serializer_class(data=request.data)
        if serializer.is_valid():
            start_date = serializer.validated_data.get('start_date')
            end_date = serializer.validated_data.get('end_date')

            if start_date < end_date:
                new_date = []

                delta = end_date - start_date
                for d in range(delta.days+1):
                    day = start_date + timedelta(days=d)
                    if day not in self.za_holidays:
                        if day.weekday() < 5:
                            new_date.append(day)

                return Response({'start_date':start_date,
                                 'end_date':end_date,
                                 'weekdays':new_date,
                                 'seconds':len(new_date)*32400})

            else:
                error_message = f'start date must be less than end date'
                return Response({'start_date':start_date,
                                 'end_date':end_date,
                                 'message':error_message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def calculateseconds(self, start_date, end_date):
        seconds = (end_date - start_date).total_seconds()
        return seconds
