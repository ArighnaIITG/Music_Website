#from django.http import HttpResponse ... http response is inbuilt in render template shortcut

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Album

def index(request):
    all_albums = Album.objects.all() #Connecting albums to the database
    #template = loader.get_template('music/index.html') ...used when we imported loader
    context = {
        'all_albums' : all_albums
    }
    #return HttpResponse(template.render(context, request))...used when we imported loader
    return render(request, 'music/index.html', context)

def detail(request,album_id):
    #try:
    #    album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
    #    raise Http404("Album does not exist")
    
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album' : album})

