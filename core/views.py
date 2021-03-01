from django.shortcuts import render
from .models import Album
from .models import Artist


# Create your views here.


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album/post_album.html', {'albums': albums})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'album/artist_list.html', {'artists': artists})