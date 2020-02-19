from .models import note
def get_files(request):
    return {
        'files': note.objects.all()
    }
