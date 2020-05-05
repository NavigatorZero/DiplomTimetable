from .models import MainTable
from .models import MainTable, CafedraClasses


class Rasp:

    # Функция устанавливает в главную таблицу преподователей
    def setTeacher(Table, PrepodArray):
        for x in range(len(Table)):
            for PrepodTable in PrepodArray:
                day = PrepodTable.filter(Date=Table[x].vremya)
                if day and Table[x].Prepod == "":
                    mainTableday = Table.filter(vremya=Table[x].vremya)
                    for lesson in day:
                        for mainDay in mainTableday:

                            if lesson.LessonNumber == mainDay.NLecii:
                                obj = Table.get(pk=mainDay.id)
                                obj.Prepod = lesson.teacher.last_name + " " + lesson.teacher.first_name  # надо откуда то брать имя препода
                                obj.teacherId = lesson.teacher
                                obj.save()

    # функция устанавливает предмет в главную таблицу
    def setSubject(Table, studyPlan, hours):
        exTable=Table.exclude(Prepod="")

        for x in range(len(exTable)):
            for y in range(len(studyPlan)):
                print("eto TABLICA ID" + str(exTable[x]))
                print("eto teacher ID"+str( exTable[x].teacherId))
                print("eto study plan ID" + str(studyPlan[y].teacher))
                if exTable[x].teacherId == studyPlan[y].teacher and hours > 0:
                    obj = MainTable.objects.get(pk=exTable[x].id)
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
