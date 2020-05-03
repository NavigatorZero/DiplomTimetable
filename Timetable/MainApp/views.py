from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.db.models import Sum, Max, Count, Avg
from .Rasp import *
import datetime
from django.contrib.auth.models import User
from .Forms import NameForm

from django.db import connection, transaction
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.apps import apps


def Main_list(request):
    listOfTeachers = []
    if request.method == 'POST' and 'email' in request.POST:
        UserModel = get_user_model()
        user = UserModel.objects.get(email=request.POST['email'])
        print(user)
        user = authenticate(request, username=user, password=request.POST['password'])

        if user is not None:
            login(request, user)
            if user.is_staff:
                modelName = user.username
                Model = apps.get_model('MainApp', modelName)

                teacherTable = Model.objects.all()
                Result = MainTable.objects.all()
                return render(request, 'test.html', {'posts': Result, 'teacherTable': teacherTable})
        else:
            print('no Auth')

    if request.method == 'POST' and 'logout' in request.POST:
        logout(request)

    if request.method == 'POST' and 'erase' in request.POST:
        MainTable.objects.all().delete()
        group1 = studyPlanPE61.objects.all()
        for x in range(len(group1)):
            group1[x].remaningLectures = group1[x].hours
            group1[x].save()

    if request.method == 'POST' and 'fill' in request.POST:
        cursor = connection.cursor()
        # Data modifying operation - commit required
        cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'MainApp_maintable'")
        transaction.commit()
        opa = []
        for i in range(50):
            test = MainTable()
            test.Auditoriya = ""
            test.NLecii = ""
            test.Predmet = ""
            test.Prepod = ""
            test.Podgruppa = ""
            test.vremya = datetime.datetime.now()

            opa.append(test)
            MainTable.objects.bulk_create(opa)

    if request.method == 'POST' and 'scheduleDay' in request.POST:
        print(request.POST['scheduleDay'])
        oneDayRasp = MainTable.objects.filter(vremya=request.POST['scheduleDay'])

        return render(request, 'main_table.html', {'posts': oneDayRasp, 'dayRasp': request.POST['scheduleDay']})

    semestrdays = 121  # кол-во дней в семестре
    semestrHours = 726  # часов в семестре
    subjectArray = [
        "Математика", "Физика", "География"
    ]

    AllHours = studyPlanPE61.objects.aggregate(Sum('hours')).get('hours__sum',
                                                                 0.00)  # кол-во часов одной группы в семестр по всем дисциплинам
    Academic = MainTable.objects.all()

    PrepodArray = [teacher1.objects.filter(isBusy="True"), teacher2.objects.filter(isBusy="True"),
                   teacher3.objects.filter(isBusy="True"),
                   teacher4.objects.filter(isBusy="True"), teacher5.objects.filter(isBusy="True")]

    Rasp.setTeacher(Academic, PrepodArray)  # Записываем преподователя на основе его выбора
    for word in subjectArray:

        if studyPlanPE61.objects.filter(subject=word).exists():
            HoursByDiscipline = studyPlanPE61.objects.filter(subject=word).aggregate(Sum('hours')).get('hours__sum',
                                                                                                       0.00)  # кол-во часов по дисциплине
            hours = CustomValues()
            hours.alias = "HoursByDiscipline " + word
            hours.value = HoursByDiscipline
            hours.save()
            Rasp.setSubject(Academic, studyPlanPE61.objects.filter(subject=word),
                            HoursByDiscipline)  # Записываем предмет на основе кол-ва часов

    Result = MainTable.objects.all()

    return render(request, 'test.html', {'posts': Result, })
