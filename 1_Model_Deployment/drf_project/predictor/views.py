from django.shortcuts import render

# Create your views here.
import os
import joblib
import rest_framework

model = joblib.load('intent_classifier.pkl')

@api_view
def predict(request):
    if request.get():
        input = request.get()
    
    output = model.predict(input)

    return output