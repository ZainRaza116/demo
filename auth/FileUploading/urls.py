from django.urls import path
from .views import webcam_view , file_uploading 

urlpatterns = [
    path('fileupload/', file_uploading, name='file_uploading'),
    path('', webcam_view, name='webcam_view'),  # Map the root URL to webcam_view
]
