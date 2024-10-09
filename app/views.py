from django.views import View
from django.shortcuts import render
import joblib
import numpy as np

# Load the model
model = joblib.load('models/heart_disease_prediction')

class Home(View):
    def get(self, request):
        return render(request, 'index.html')

class Predict(View):
    def post(self, request):
        # Get form data
        male = request.POST['male']
        age = int(request.POST['age'])
        currentSmoker = request.POST['currentSmoker']
        cigsPerDay = float(request.POST['cigsPerDay'])
        BPMeds = request.POST['BPMeds']
        prevalentStroke = request.POST['prevalentStroke']
        prevalentHyp = request.POST['prevalentHyp']
        diabetes = request.POST['diabetes']
        totChol = float(request.POST['totChol'])
        sysBP = float(request.POST['sysBP'])
        diaBP = float(request.POST['diaBP'])
        BMI = float(request.POST['BMI'])
        heartRate = float(request.POST['heartRate'])
        glucose = float(request.POST['glucose'])

        # Prepare features array
        male_encoded = 1 if male == "1" else 0
        currentSmoker_encoded = 1 if currentSmoker == "1" else 0
        BPMeds_encoded = 1 if BPMeds == "1" else 0
        prevalentStroke_encoded = 1 if prevalentStroke == "1" else 0
        prevalentHyp_encoded = 1 if prevalentHyp == "1" else 0
        diabetes_encoded = 1 if diabetes == "1" else 0

        features = np.array([[male_encoded, age, currentSmoker_encoded, cigsPerDay, BPMeds_encoded,
                              prevalentStroke_encoded, prevalentHyp_encoded, diabetes_encoded,
                              totChol, sysBP, diaBP, BMI, heartRate, glucose]])

        # Make prediction
        result = model.predict(features)
        prediction_text = "The Patient has Heart Disease" if result[0] == 1 else "The Patient has No Heart Disease"

        return render(request, 'index.html', {'prediction': prediction_text})
