from django import forms
from .models import Artist
from .models import Album

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'image']

        
class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'genre']