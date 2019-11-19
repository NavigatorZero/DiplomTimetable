from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import AcademicPlan,Teachers,Cafedra,Auditoriy,Group,Subject

def Main_list(request):
        Academic=AcademicPlan.objects.all()
        Tchers=Teachers.objects.all()
        Cfedra=Cafedra.objects.all()
        Aditoriy=Auditoriy.objects.all()
        Grup=Group.objects.all()
        Subjct=Subject.objects.all()
        return render(request, 'test.html', {'posts': Academic})
