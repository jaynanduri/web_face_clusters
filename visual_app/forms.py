from django import forms
from .models import FaceImage


class FaceImageForm(forms.ModelForm):
    class Meta:
        model = FaceImage
        fields = ['name', 'face_img']

