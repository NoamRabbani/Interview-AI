from django.http import HttpResponse, Http404
from django.shortcuts import render

from Interviewer.static.Interviewer.python import speechToText

def index(request):
    return render(request, 'Interviewer/index.html')

def recorder(request):
    return render(request, 'Interviewer/recorder.html')

def recorderWorker(request):
    return render(request, 'Interviewer/recorderWorker.js')

def analyzeSpeech(request):
    try:
        user_speech_b64code = request.POST['user_speech_b64code']
    except:
        raise Http404

    textFromSpeech = speechToText.speech_to_text(user_speech_b64code)

    return render(request, 'Interviewer/analyzeSpeech.html')
