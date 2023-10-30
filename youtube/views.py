from django.shortcuts import render
from .forms import DownloadForm
import youtube_dl as yt
import re as regularExpression

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,"about.html")

def huongdan(request):
    return render(request,"huongdan.html")