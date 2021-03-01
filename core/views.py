from django.shortcuts import render
from .models import Album

# Create your views here.


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album/post_album.html', {'albums': albums})