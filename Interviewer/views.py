from django.http import HttpResponse, Http404
from django.shortcuts import render

from Interviewer.static.Interviewer.python import speechToText

def index(request):
    return render(request, 'Interviewer/index.html')

def recorder(request):
    return render(request, 'Interviewer/recorder.html')

def recorderWorker(request):
    return render(request, 'Interviewer/recorderWorker.js')

def webcamWorker(request):
    return render(request, 'Interviewer/webcamWorker.js')

def analyzeSpeech(request):
    try:
        user_speech_b64code = request.POST['user_speech_b64code']
    except:
        raise Http404

    dataFromSpeech = speechToText.speech_to_text(user_speech_b64code)

    average_velocity = dataFromSpeech['average_velocity']
    speech_speed = dataFromSpeech['speech_speed']
    print(average_velocity)

    context = {
        "average_velocity": average_velocity,
        "speech_speed": speech_speed,
    }

    return render(request, 'Interviewer/analyzeSpeech.html' , context)
