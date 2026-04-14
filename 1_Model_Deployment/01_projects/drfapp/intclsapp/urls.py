from django.urls import path
from .views import IntclsPredictView, StdclsPredictView

urlpatterns = [
    path('intent-pred', IntclsPredictView.as_view(), name='intentpredictview'),
    path('result-pred', StdclsPredictView.as_view(), name='resultpredictview'),
]