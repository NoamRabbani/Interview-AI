from django.http import HttpResponse, Http404
from django.shortcuts import render
import base64

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
        user_photo_url = request.POST['user_photo_url']
    except:
        raise Http404

    dataFromSpeech = speechToText.speech_to_text(user_speech_b64code)

    average_velocity = dataFromSpeech['average_velocity']
    speech_speed = dataFromSpeech['speech_speed']
    print(average_velocity)

    #webcam snapshot data
    user_photo_url = user_photo_url[user_photo_url.find(",")+1:]
    imgdata = base64.b64decode(user_photo_url)
    filename = 'user_photo.png'
    with open(filename, 'wb') as f:
        f.write(imgdata)
    print(speechToText.pic_anly())

    context = {
        "average_velocity": average_velocity,
        "speech_speed": speech_speed,
    }

    return render(request, 'Interviewer/analyzeSpeech.html' , context)
