from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MainTable

def Main_list(request):
    Table = MainTable.objects.all()
    return render(request, 'test.html', {'posts': Table})
