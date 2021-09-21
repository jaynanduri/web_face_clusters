from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import UploadForm
from .models import Upload
import os


def home_view(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context = {'form': form}
    return render(request, 'home.html', context)


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    return render(request, 'signup.html', {'form': form})


'''
def result(request):
    current_user=request.user
    uploaded=Upload.objects.filter(name=current_user).order_by('-id')[0]
    if uploaded.company_list!='' and uploaded.company_name='':
        comp_list=os.path.join('media',str(uploaded.company_list))
        ## code for file processing
        ##input files will be in media/InputFiles
    else:
        comp_name=str(uploaded.company_name)
        ## code for single company
        ##update the output excel file path in status.html
        ## put output excel file in 'static/files/output'
'''
