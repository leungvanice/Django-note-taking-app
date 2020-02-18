from .models import note
from django import forms


class createNoteForm(forms.ModelForm):
    class Meta:
        model = note
        fields = ['title', 'content']

class editNoteForm(forms.Form):
    class Meta:
        model = note
        fields = ['title', 'content']