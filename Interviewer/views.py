from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'Interviewer/index.html')

def recorder(request):
    return render(request, 'Interviewer/recorder.html')

def recorderWorker(request):
    return render(request, 'Interviewer/recorderWorker.js')
