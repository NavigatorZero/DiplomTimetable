from django import forms

class TeacherForm(forms.Form):

    lessonNumber = forms.CharField(label='Номер занятия', max_length=100);
    date = forms.DateField(label='Дата')
