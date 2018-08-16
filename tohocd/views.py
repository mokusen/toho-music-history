from django.shortcuts import render, redirect
from .forms import FindForm, DetailForm

def index(request):
    return render(request, 'tohocd/index.html')
