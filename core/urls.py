from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('artists', views.artist_list, name='artist_list'),
    # path('artists_albums', views.artist_albums, name='artist_albums')
]