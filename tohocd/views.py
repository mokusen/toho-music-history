from django.shortcuts import render, redirect
from .forms import FindForm, DetailForm
from .services import songService, circleService
from .utils import handleParam

def index(request):
    return render(request, 'tohocd/index.html')

def search(request, num=1):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
        song = songService.get_songs_byOR(word)
        params = handleParam.create_param(song, num, form, 'form')
    else:
        form = FindForm()
        params = {"form":form, "max": 0}
    return render(request, 'tohocd/search.html', params)

def detail(request, num=1):
    if len(request.GET) != 0:
        word_dict = handleParam.check_param(request.GET)
        form = DetailForm(word_dict)
        song = songService.get_songs_byAND(word_dict)
        params = handleParam.create_param(song, num, form, 'form')
    else:
        form = DetailForm()
        params = {"form":form, "max": 0}
    return render(request, 'tohocd/detail.html', params)

def cd(request):
    return render(request, 'tohocd/cd.html')

def circle(request, num=1):
    if 'find' in request.GET:
        word = request.GET['find']
        form = FindForm(request.GET)
    else:
        word = ""
        form = FindForm()
    song = circleService.get_circles(word)
    params = handleParam.create_param(song, num, form, 'form')
    return render(request, 'tohocd/circle.html', params)

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
