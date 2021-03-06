from .models import MainTable
from .models import MainTable, CafedraClasses


class Rasp:

    # Функция устанавливает в главную таблицу преподователей
    def setTeacher(Table, PrepodArray, priority):
        print(priority)
        for x in range(len(Table)):
            for PrepodTable in PrepodArray:
                day = PrepodTable.filter(Date=Table[x].vremya)
                if day and Table[x].Prepod == "":
                    mainTableday = Table.filter(vremya=Table[x].vremya)
                    for lesson in day:
                        for mainDay in mainTableday:
                            if lesson.LessonNumber == mainDay.NLecii:
                                if priority == 1:
                                    obj = Table.get(pk=mainDay.id)
                                    obj.Prepod = lesson.teacher.last_name + " " + lesson.teacher.first_name  # надо откуда то брать имя препода
                                    obj.teacherId = lesson.teacher
                                    obj.save()

                                if priority == 2:
                                    isBusy = MainTable.objects.filter(NLecii=mainDay.NLecii, vremya=mainDay.vremya)
                                    if isBusy:
                                        obj = Table.get(pk=mainDay.id + 1)
                                        obj.Prepod = lesson.teacher.last_name + " " + lesson.teacher.first_name  # надо откуда то брать имя препода
                                        obj.teacherId = lesson.teacher
                                        obj.save()

    # функция устанавливает предмет в главную таблицу
    def setSubject(Table, studyPlan, hours):
        exTable = Table.exclude(Prepod="")
        print(studyPlan)
        for x in range(len(exTable)):
            for y in range(len(studyPlan)):
                if exTable[x].teacherId == studyPlan[y].teacher and hours > 0:
                    obj = Table.get(pk=exTable[x].id)
                    hoursType = studyPlan[y].hours

                    if studyPlan[y].typeSubject == "Лекция" and obj.Auditoriya == "" and studyPlan[
                        y].remaningLectures > 0:
                        clases = CafedraClasses.objects.filter(AllowedLections="True")
                        obj.Predmet = studyPlan[y].subject
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()
                        studyPlan[y].remaningLectures -= 1
                        studyPlan[y].save()
                        hours -= 1
                        continue

                    if studyPlan[y].typeSubject == "Практика" and obj.Auditoriya == "" and studyPlan[
                        y].remaningLectures > 0:
                        clases = CafedraClasses.objects.filter(AllowedPractice="True")
                        obj.Predmet = studyPlan[y].subject
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()
                        studyPlan[y].remaningLectures -= 1
                        studyPlan[y].save()
                        hours -= 1
                        continue

                    if studyPlan[y].typeSubject == "ЛабРабота" and obj.Auditoriya == "" and studyPlan[
                        y].remaningLectures > 0:
                        clases = CafedraClasses.objects.filter(AllowedLabs="True")
                        obj.Predmet = studyPlan[y].subject
                        obj.Auditoriya = clases[0].ClassName
                        obj.Podgruppa = studyPlan[y].typeSubject
                        obj.save()

                        studyPlan[y].remaningLectures -= 1
                        studyPlan[y].save()
                        hours -= 1
                        continue

    def lastIterate(Table,studyPlan):
        Table = Table.filter(Prepod__exact='')
        teacherId = studyPlan[0].teacher
        for x in Table:
            x.Prepod = teacherId.last_name + " " + teacherId.first_name
            lections = studyPlan.filter(typeSubject="Лекция")[0].remaningLectures
            practice = studyPlan.filter(typeSubject="Практика")[0].remaningLectures
            for type in studyPlan:
                if type.typeSubject == "Лекция" and type.remaningLectures > 0:
                    clases = CafedraClasses.objects.filter(AllowedLections="True")
                    x.Predmet = type.subject
                    x.Auditoriya = clases[0].ClassName
                    x.Podgruppa = type.typeSubject
                    x.save()
                    type.remaningLectures -= 1
                    type.save()
                    continue
                if type.typeSubject == "Практика" and type.remaningLectures > 0 and lections == 0:
                    clases = CafedraClasses.objects.filter(AllowedPractice="True")
                    x.Predmet = type.subject
                    x.Auditoriya = clases[0].ClassName
                    x.Podgruppa = type.typeSubject
                    x.save()
                    type.remaningLectures -= 1
                    type.save()

                    continue
                if type.typeSubject == "ЛабРабота" and type.remaningLectures > 0 and lections == 0 and practice == 0:
                    clases = CafedraClasses.objects.filter(AllowedLabs="True")
                    x.Predmet = type.subject
                    x.Auditoriya = clases[0].ClassName
                    x.Podgruppa = type.typeSubject
                    x.save()
                    type.remaningLectures -= 1
                    type.save()

                    continue
