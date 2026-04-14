from django.urls import path
from .views import StudentResultPredictView

urlpatterns = [
    path('result-pred', StudentResultPredictView.as_view(), name='resultpred'),
]
