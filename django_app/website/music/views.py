from django.http import HttpResponse
from .models import Album


def index(request):

    html = ''
    all_albums = Album.objects.all()
    for album in all_albums:
        url = f'/music/{str(album.id)}/'
        html += f'<a href={url}>{album.album_title}</a><br>'
    return HttpResponse(html)

def by_album_id(request, album_id):
    return HttpResponse(f"<h1>Details for Album : {album_id}")
