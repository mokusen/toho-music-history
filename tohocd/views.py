from django.shortcuts import render, redirect
from .forms import FindForm, DetailForm
from .services import songService
from .utils import createParam

def index(request):
    return render(request, 'tohocd/index.html')

def search(request, num=1):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
        song = songService.get_songs(word)
        params = createParam.create_param(song, form, num)
    else:
        form = FindForm()
        params = {"form":form}
    return render(request, 'tohocd/search.html', params)

def detail(request):
    return render(request, 'tohocd/detail.html')

def cd(request):
    return render(request, 'tohocd/cd.html')

def circle(request):
    return render(request, 'tohocd/circle.html')

def vocal(request):
    return render(request, 'tohocd/vocal.html')

def lyric(request):
    return render(request, 'tohocd/lyric.html')

def arrange(request):
    return render(request, 'tohocd/arrange.html')

def orisong(request):
    return render(request, 'tohocd/oriSong.html')

def oriwork(request):
    return render(request, 'tohocd/oriWork.html')
