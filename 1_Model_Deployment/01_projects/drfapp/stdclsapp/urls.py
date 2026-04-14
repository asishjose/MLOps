from django.urls import path
from .views import StdclsPredictView

urlpatterns = [
    path('result', StdclsPredictView.as_view(), name='studentresultpred'),
]