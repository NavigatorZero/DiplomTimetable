from django.shortcuts import render
import datetime

from django.apps import apps
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.db import connection, transaction
from django.db.models import Sum
from django.shortcuts import render
from django.http import JsonResponse
from .Rasp import *
from .models import *
from django.forms.models import model_to_dict
from django.core import serializers
from datetime import date, timedelta


def Main_list(request):
    listOfTeachers = []
    if request.method == 'POST':
        variables = request.POST

        if request.POST.get("lessonNumber") or request.POST.get("teacherRecordId"):
            modelName = request.user.username
            Model = apps.get_model('MainApp', modelName)

            if request.POST.get("teacherRecordId"):
                Model.objects.filter(id=request.POST['teacherRecordId']).delete()
            else:
                if Model.objects.filter(LessonNumber=request.POST.get('lessonNumber'), Date=request.POST.get('day')):
                    print("who who who")
                    return render(request, 'modal_table.html', {"teacherTable": Model.objects.all(), "error": True})
                TeacherLesson = Model()
                TeacherLesson.LessonNumber = request.POST['lessonNumber']
                TeacherLesson.Date = request.POST['day']
                TeacherLesson.teacher = request.user
                TeacherLesson.save()

            return render(request, 'modal_table.html', {"teacherTable": Model.objects.all()}, )

        if 'email' in variables:
            UserModel = get_user_model()
            user = UserModel.objects.get(email=variables['email'])
            print(user)
            user = authenticate(request, username=user, password=variables['password'])

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

        if 'logout' in variables:
            logout(request)

        if 'erase' in variables:
            MainTable.objects.all().delete()
            group1 = studyPlanPE61.objects.all()
            for x in range(len(group1)):
                group1[x].remaningLectures = group1[x].hours
                group1[x].save()

        if 'fill' in variables:
            cursor = connection.cursor()
            # Data modifying operation - commit required
            cursor.execute("UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'MainApp_maintable'")
            transaction.commit()

            sdate = date(2020, 9, 1)  # start date
            edate = date(2020, 10, 1)  # end date

            delta = edate - sdate  # as timedelta

            for i in range(delta.days + 1):
                day = sdate + timedelta(days=i)

                opa = []
                for d in range(6):
                    test = MainTable()
                    test.Auditoriya = ""
                    test.NLecii = d + 1
                    test.Predmet = ""
                    test.Prepod = ""
                    test.Podgruppa = ""
                    test.vremya = day
                    opa.append(test)

                MainTable.objects.bulk_create(opa)



            semestrdays = 121  # кол-во дней в семестре
            semestrHours = 726  # часов в семестре
            subjectArray = [
                "Математика", "Физика", "География"
            ]

            AllHours = studyPlanPE61.objects.aggregate(Sum('hours')).get('hours__sum',
                                                                         0.00)  # кол-во часов одной группы в семестр по всем дисциплинам
            Academic = MainTable.objects.all()

            PrepodArray = [teacher1.objects.all(), teacher2.objects.all(),
                           teacher3.objects.all(),
                           teacher4.objects.all(), teacher5.objects.all()]

            Rasp.setTeacher(Academic, PrepodArray)  # Записываем преподователя на основе его выбора
            for word in subjectArray:

                if studyPlanPE61.objects.filter(subject=word).exists():
                    HoursByDiscipline = studyPlanPE61.objects.filter(subject=word).aggregate(Sum('hours')).get(
                        'hours__sum',
                        0.00)  # кол-во часов по дисциплине
                    hours = CustomValues()
                    hours.alias = "HoursByDiscipline " + word
                    hours.value = HoursByDiscipline
                    hours.save()
                    print('yoyoy')
                    Rasp.setSubject(Academic, studyPlanPE61.objects.filter(subject=word),
                                    HoursByDiscipline)  # Записываем предмет на основе кол-ва часов

        if request.method == 'POST' and 'scheduleDay' in request.POST:
            print(request.POST['scheduleDay'])
            oneDayRasp = MainTable.objects.filter(vremya=request.POST['scheduleDay'])

            return render(request, 'main_table.html', {'posts': oneDayRasp, 'dayRasp': request.POST['scheduleDay']})

    Result = MainTable.objects.all()

    return render(request, 'test.html', {'posts': Result, })
