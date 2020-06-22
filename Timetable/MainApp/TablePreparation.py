from datetime import date, timedelta

from django.db.models import Sum

from .Rasp import *
from .UserInterface import *


class TablePreparation:

    def Erase(self):
        MainTable.objects.all().delete()
        group1 = studyPlanPE61.objects.all()
        for x in range(len(group1)):
            group1[x].remaningLectures = group1[x].hours
            group1[x].save()

        MainTableGroup2.objects.all().delete()
        group2 = studyPlanGroup2.objects.all()
        for x in range(len(group2)):
            group2[x].remaningLectures = group2[x].hours
            group2[x].save()

    def Fill(self):

        sdate = date(2020, 9, 1)  # start date
        edate = date(2020, 9, 30)  # end date
        delta = edate - sdate  # as timedelta
        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)

            # заполняем первую группу
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

            # заполняем вторую группу
            group2Main = []
            for d in range(6):
                test = MainTableGroup2()
                test.Auditoriya = ""
                test.NLecii = d + 1
                test.Predmet = ""
                test.Prepod = ""
                test.Podgruppa = ""
                test.vremya = day
                group2Main.append(test)
            MainTableGroup2.objects.bulk_create(opa)

        semestrdays = 121  # кол-во дней в семестре
        semestrHours = 726  # часов в семестре
        subjectArray = CustomValues.objects.filter(alias="subject")

        AllHours = studyPlanPE61.objects.aggregate(Sum('hours')).get('hours__sum',
                                                                     0.00)  # кол-во часов одной группы в семестр по всем дисциплинам
        mainTable1 = MainTable.objects.all()
        mainTable2 = MainTableGroup2.objects.all()

        PrepodArray = [teacher1.objects.all(), teacher2.objects.all(),
                       teacher3.objects.all(),
                       teacher4.objects.all(), teacher5.objects.all()]

        Rasp.setTeacher(mainTable1, PrepodArray,
                        1)  # Записываем преподователя в группу 1 на основе его выбора
        Rasp.setTeacher(mainTable2, PrepodArray,
                        2)  # Записываем преподователя в группу 2 на основе его выбора
        for word in subjectArray:
            if studyPlanPE61.objects.filter(subject=word.value).exists():
                HoursByDiscipline = studyPlanPE61.objects.filter(subject=word.value).aggregate(Sum('hours')).get(
                    'hours__sum',
                    0.00)  # кол-во часов по дисциплине
                Rasp.setSubject(mainTable1, studyPlanPE61.objects.filter(subject=word.value),
                                HoursByDiscipline)  # Записываем предмет на основе кол-ва часов

                ReminingHours = studyPlanPE61.objects.filter(subject=word.value).aggregate(
                    Sum('remaningLectures')).get(
                    'remaningLectures__sum', 0.00)
                if ReminingHours > 0:
                    print("here")
                    Rasp.lastIterate(mainTable1, studyPlanPE61.objects.filter(subject=word.value),
                                     )

            if studyPlanGroup2.objects.filter(subject=word.value).exists():
                HoursByDiscipline = studyPlanGroup2.objects.filter(subject=word.value).aggregate(
                    Sum('hours')).get(
                    'hours__sum',
                    0.00)  # кол-во часов по дисциплине
                Rasp.setSubject(mainTable2, studyPlanGroup2.objects.filter(subject=word.value),
                                HoursByDiscipline)  # Записываем предмет на основе кол-ва часов

                ReminingHours = studyPlanGroup2.objects.filter(subject=word.value).aggregate(
                    Sum('remaningLectures')).get(
                    'remaningLectures__sum', 0.00)
                if ReminingHours > 0:
                    print("here")
                    Rasp.lastIterate(mainTable1, studyPlanGroup2.objects.filter(subject=word.value),
                                     )
