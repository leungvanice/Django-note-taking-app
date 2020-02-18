from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy
# Create your models here.
class note(models.Model):
    title = models.CharField(max_length=100) 
    content = models.TextField() 
    created_date = models.DateTimeField(timezone.now()) 
    modified_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 


