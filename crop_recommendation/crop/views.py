import os
import joblib
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages


# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "ml_models/random_forest_model_1.pkl")
ENCODER_PATH = os.path.join(BASE_DIR, "ml_models/label_encoder.pkl")

# Load model and label encoder
model = joblib.load(MODEL_PATH)
label_encoder = joblib.load(ENCODER_PATH)

def predict(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        try:
            # Extract data from POST request
            data = request.POST
            features = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
            input_data = [[
                float(data.get('N')),
                float(data.get('P')),
                float(data.get('K')),
                float(data.get('temperature')),
                float(data.get('humidity')),
                float(data.get('ph')),
                float(data.get('rainfall'))
            ]]

            # Make prediction
            prediction = model.predict(input_data)
            predicted_crop = label_encoder.inverse_transform(prediction)[0]

            return JsonResponse({'predicted_crop': predicted_crop})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return render(request, 'crop_predict.html')


def homepage(request):
    return render(request,'agribot-website.html')



def chatbot(request):
    return render(request,'agribot-redesign.html')