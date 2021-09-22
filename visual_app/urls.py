from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'image_upload$', upload_query_image, name='image_upload'),
    url(r'success$', success, name='success'),
    url(r'images$', display_image, name='images'),
]
