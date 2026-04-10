from django.urls import path, include
from .views import PredictView

urlpatterns = [
    path('predictdrf', PredictView.as_view(), name='Predictdrf'),
]