from django.apps import AppConfig
from django.urls import path
from . import views


class PredictionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'student'

urlpatterns = [
    path('', views.predict_performance, name='predict_salary'),  # Route to the predict_salary view
]
