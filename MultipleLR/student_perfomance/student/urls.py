from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('predict/', views.predict, name='predict'),  # Prediction page
    path('predict_performance', views.predict_performance, name='predict_performance'),  # Prediction API
]
