from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recorder$', views.recorder, name='recorder'),
    url(r'^analyzeSpeech$', views.analyzeSpeech, name='analyzeSpeech'),

    url(r'^recorderWorker.js$', views.recorderWorker, name='recorderWorker'),
    url(r'^webcamWorker.js$', views.webcamWorker, name='webcamWorker'),
]
