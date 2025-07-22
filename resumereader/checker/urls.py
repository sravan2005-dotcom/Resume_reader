from django.contrib import admin
from django.urls import path  # Ensure you import path here
from django.conf import settings
from django.conf.urls.static import static
from .views import * # If you're including views from 'checker' app

urlpatterns = [
    path('upload/', upload_resume, name='upload_resume'),  
    path('result/<int:resume_id>/', result, name='result'),
    
]

# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)