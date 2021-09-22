from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FaceImageForm
from .models import FaceImage
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def upload_query_image(request):
    if request.method == 'POST':
        form = FaceImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('images')
    else:
        form = FaceImageForm()
    return render(request, 'image_query.html', {'form': form})


def success(request):
    return HttpResponse('Successfully uploaded!!')


def display_image(request):
    if request.method == 'GET':
        face_images = FaceImage.objects.all()
        return render(request, 'display_images.html', {'face_images': face_images})

