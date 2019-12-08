from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import MainTable,Prepod1,studyPlanPE61,Prepod2
from django.db.models import Sum,Max,Count,Avg


class Rasp():
       
        def setTeacher(Table,PrepodTable,prepod2):
                for x in range(len(Table)):  
                        for y in range(len(PrepodTable)):
                                if Table[x].id==PrepodTable[y].id and Table[x].Prepod=="":
                                        obj = MainTable.objects.get(pk=Table[x].id)
                                        obj.Prepod = "Уймин А.Г"#надо откуда то брать имя препода
                                        obj.NLecii =PrepodTable[y].LessonNumber
                                        obj.vremya = PrepodTable[y].Date
                                        obj.save()

                        for y in range(len(prepod2)):
                                if Table[x].id==prepod2[y].id and Table[x].Prepod=="" :
                                        obj = MainTable.objects.get(pk=Table[x].id)
                                        obj.Prepod = "Ленин И.В"#надо откуда то брать имя препода
                                        obj.NLecii =prepod2[y].LessonNumber
                                        obj.vremya = prepod2[y].Date
                                        obj.save()
        def setSubject(Table,studyPlan,hours):
                for x in range(len(Table)):
                        for y in range(len(studyPlan)):
                                if Table[x].Prepod!="" and Table[x].Prepod in studyPlan[y].teacher and hours>0:
                                        obj = MainTable.objects.get(pk=Table[x].id)
                                        obj.Predmet=studyPlan[y].subject
                                        obj.save()
                                        hours=hours-1
                                       
                                        
              
       
def Main_list(request):
        semestrdays=121#кол-во дней в семестре
        semestrHours=726 #часов в семестре
        subjectArray=[
                "Математика","Физика","Русский язык"
        ]
        AllHours=studyPlanPE61.objects.aggregate(Sum('hours')).get('hours__sum', 0.00)#кол-во часов одной группы в семестр по всем дисциплинам

        group1=studyPlanPE61.objects.all()
        Academic=MainTable.objects.all()
        prepod1=Prepod1.objects.filter(isBusy="True")
        prepod2=Prepod2.objects.filter(isBusy="True")
       
        Rasp.setTeacher(Academic,prepod1,prepod2)#Записываем преподователя на основе его выбора
        for word in subjectArray: 
                if studyPlanPE61.objects.filter(subject=word).exists():
                        HoursByDiscipline=studyPlanPE61.objects.filter(subject=word).aggregate(Sum('hours')).get('hours__sum', 0.00)#кол-во часов по дисциплине 
                        print("hours", HoursByDiscipline)
                        Rasp.setSubject(Academic,group1,HoursByDiscipline)# Записываем предмет на основе кол-ва часов
        
        
        return render(request, 'test.html', {'posts': Academic,"groups":HoursByDiscipline,"tests":AllHours, })
