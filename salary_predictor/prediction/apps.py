from django.apps import AppConfig
from django.urls import path
from . import views


class PredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'prediction'

urlpatterns = [
    path('', views.predict_salary, name='predict_salary'),  # Route to the predict_salary view
]
