from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import UploadFileModel
# Create your views here.
def home(request):
    files=UploadFileModel.objects
    return render(request,'home.html',{'files':files})