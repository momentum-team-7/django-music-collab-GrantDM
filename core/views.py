from django.shortcuts import render
from .models import Album
from .models import Artist
# from .models import Album_title

# Create your views here.


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album/post_album.html', {'albums': albums})


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'album/artist_list.html', {'artists': artists})


# def artist_albums(request):
#     artist_album_list = Album_title.objects.all()
#     return render(request, 'album/artist_albums.html', {'artist_album_list': artist_album_list})