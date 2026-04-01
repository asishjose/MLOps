from django.urls import path
from .views import PredictView

urlpatterns = [
    path("predict/", PredictView.as_view(), name="predict"),

]

from django.urls import path, include

urlpatterns = [
    path('api/v1/', include("predictor.urls")),
]