from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class MainTable(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    NLecii = models.CharField(max_length=250)
    Predmet = models.CharField(max_length=250)

    Prepod =   models.CharField(max_length=250)
    Podgruppa = models.CharField(max_length=250)
    vremya= models.DateTimeField(auto_now_add=True)
    Auditoriya =  models.CharField(max_length=250)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

class Meta:
    ordering = ('-publish',)

def __str__(self):
    return self.title
