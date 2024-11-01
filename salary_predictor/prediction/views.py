from django.shortcuts import render
import numpy as np
from joblib import load

# Load the saved model
model = load('F:/2024/python/supervised.learning/Linear-Regression/linear_model_salary.joblib')

def predict_salary(request):
    if request.method == 'POST':
        # Get the input from the form
        experience_years = float(request.POST['experience'])

        # Ensure the input has the correct shape (e.g., [1, 2] if an intercept is needed)
        prediction_input = np.array([[1, experience_years]])  # Adding '1' for intercept

        # Make the prediction
        predicted_salary = model.predict(prediction_input)[0]

        # Send the result back to the template
        return render(request, 'predict.html', {'salary': predicted_salary})
    else:
        return render(request, 'predict.html')
