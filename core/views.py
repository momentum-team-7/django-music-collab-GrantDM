from django.shortcuts import render, get_object_or_404
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


def artist_albums(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'album/artist_albums.html', {'artist': artist})


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    return render(request, 'album/artist_detail.html', {'artist': artist})