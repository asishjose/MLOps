from django.urls import path
from .views import BatchPredictView, PredictView

urlpatterns = [
    path("predict/", PredictView.as_view(), name="predict"),
    path("predict/batch/", BatchPredictView.as_view(), name="predict-batch"),
]
