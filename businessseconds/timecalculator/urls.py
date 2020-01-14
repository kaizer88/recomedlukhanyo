from django.urls import path
from .views import CalculateTime


urlpatterns = [
    path('time-view/', CalculateTime.as_view()),
]