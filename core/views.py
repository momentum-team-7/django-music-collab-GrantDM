from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import AlbumForm
from .forms import ArtistForm
from .models import Album
from .models import Artist

# Create your views here.


def Homepage(request):
    return render(request, 'album/Homepage.html', {})


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


def add_album(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AlbumForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AlbumForm()

    return render(request, 'album/add_album.html', {'form': form})


def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArtistForm()
    return render(request, 'album/add_artist.html', {'form': form})


def edit_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = ArtistForm(instance=artist)
    return render(request, 'album/edit_artist.html', {'form': form, 'artist':artist })


def edit_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = AlbumForm(instance=album)
    return render(request, 'album/edit_album.html', {'form': form, 'album':album })


def delete_artist(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return HttpResponseRedirect('/')


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    return HttpResponseRedirect('/')
