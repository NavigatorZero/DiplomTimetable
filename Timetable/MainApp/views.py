from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MainTable, teacher1, studyPlanPE61, teacher2,CafedraClasses
from django.db.models import Sum, Max, Count, Avg
from .Rasp import *
from django.contrib.auth.models import User




def Main_list(request):

    semestrdays = 121  # кол-во дней в семестре
    semestrHours = 726  # часов в семестре
    subjectArray = [
        "Математика", "Физика", "Гегорафия"
    ]


    AllHours = studyPlanPE61.objects.aggregate(Sum('hours')).get('hours__sum',
                                                                 0.00)  # кол-во часов одной группы в семестр по всем дисциплинам

    group1 = studyPlanPE61.objects.all()
    Academic = MainTable.objects.all()

    prepod1 = teacher1.objects.filter(isBusy="True")

    prepod2 = teacher2.objects.filter(isBusy="True")


    PrepodArray = [prepod1, prepod2]

    Rasp.setTeacher(Academic, PrepodArray)  # Записываем преподователя на основе его выбора
    for word in subjectArray:

        if studyPlanPE61.objects.filter(subject=word).exists():
            HoursByDiscipline = studyPlanPE61.objects.filter(subject=word).aggregate(Sum('hours')).get('hours__sum',
                                                                                                       0.00)  # кол-во часов по дисциплине
            print("hours", HoursByDiscipline)
            Rasp.setSubject(Academic, group1, HoursByDiscipline)  # Записываем предмет на основе кол-ва часов

    return render(request, 'test.html', {'posts': Academic, "groups": prepod1, "tests": AllHours, })
