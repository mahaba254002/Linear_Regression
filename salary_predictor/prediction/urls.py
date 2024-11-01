from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict_salary, name='predict_salary'),  # Route to the predict_salary view
]
