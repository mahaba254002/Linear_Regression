from django.shortcuts import render
from django.http import JsonResponse
import json
import numpy as np
from django.views.decorators.csrf import csrf_exempt
from joblib import load

# Load the saved model
try:
    model = load('F:/2024/python/supervised.learning/Linear-Regression/MultipleLR/student_performance.joblib')
except FileNotFoundError:
    raise FileNotFoundError("Model file not found. Please verify the file path.")

def index(request):
    # Render the prediction page
    return render(request, 'student/index.html')

def predict(request):
    # Render the prediction page
    return render(request, 'student/predict.html')

@csrf_exempt
def predict_performance(request):
    if request.method == 'POST':
        try:
            # Parse JSON data from the request
            data = json.loads(request.body)

            # Extract features and validate input data
            try:
                features = np.array([
                    float(data['x1']),  # hours studied
                    float(data['x2']),  # previous scores
                    float(data['x3']),  # activities (0 or 1)
                    float(data['x4']),  # sleep hours
                    float(data['x5'])   # question papers practiced
                ]).reshape(1, -1)
            except (KeyError, ValueError):
                return JsonResponse({'error': 'Invalid input data. Please check all required fields.'}, status=400)

            # Make prediction
            predicted_index = model.predict(features)[0]
            return JsonResponse({'predictedIndex': round(predicted_index, 2)})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
