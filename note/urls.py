from django.urls import path 
from . import views 
urlpatterns = [
    path('', views.home, name='note-home'),
    path('<int:pk>/', views.NoteDetailView.as_view(), name='note-detail'),
    path('create/', views.createNote, name='note-create'), 
    path('<int:pk>/edit/', views.editNote.as_view(), name='note-edit')
]