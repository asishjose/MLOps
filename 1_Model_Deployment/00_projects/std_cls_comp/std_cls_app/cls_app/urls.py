from django.urls import path
from .views import PredictView

urlpatterns = [
    path('student', PredictView.as_view(), name='predictview')
]