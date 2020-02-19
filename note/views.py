from django.shortcuts import render
from .models import note
from django.views.generic import DetailView, UpdateView
from .forms import createNoteForm, editNoteForm
from django.urls import reverse_lazy

# Create your views here.
def home(request): 
    return render(request, 'note/index.html', {'notes': note.objects.all()})


class NoteDetailView(DetailView):
    model = note 
    
def createNote(request):
    if request.method == 'POST': 
        form = createNoteForm(request.POST) 

        if form.is_valid():  
            title = form.cleaned_data.get('title')
            print(title) 
    else: 
        form = createNoteForm() 
    return render(request, 'note/note_form.html', {'form': form})
    

class editNote(UpdateView):
    model = note 
    fields = ['title', 'content']
    template_name_suffix = '_update_form'
    
    def get_success_url(self):
        noteId = self.kwargs['pk']
        return reverse_lazy('note-detail', kwargs={'pk': noteId})
    
