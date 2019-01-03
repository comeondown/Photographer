from .models import Album

def global_albums_context_processor(request):
    albums = Album.objects.all()
    print(albums)
    context = {
        'albums': albums
    }
    return context