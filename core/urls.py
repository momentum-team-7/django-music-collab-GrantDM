from django.urls import path
from django.http import HttpResponseRedirect

from . import views


urlpatterns = [
    path('', views.Homepage, name="Homepage"),
    path('albums', views.album_list, name='album_list'),
    path('artists', views.artist_list, name='artist_list'),
    path('artists/<int:pk>/', views.artist_albums, name='artist_albums'),
    path('details/<int:pk>/', views.artist_detail, name='artist_detail'),
    path('albums/new', views.add_album, name='add_album'),
    path('artist/new', views.add_artist, name='add_artist'),
    path('artists/<int:pk>/edit', views.edit_artist, name="edit-artist"),
    path('album/<int:pk>/edit', views.edit_album, name="edit-album"),
    path('artists/<int:pk>/delete', views.delete_artist, name="delete-artist"),
    path('album/<int:pk>/delete', views.delete_album, name="delete-album"),

]