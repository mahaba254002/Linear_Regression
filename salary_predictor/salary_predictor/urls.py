from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('prediction.urls')),  # Include the URLs from the 'prediction' app
]
