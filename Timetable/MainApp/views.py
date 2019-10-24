from django.shortcuts import render, get_object_or_404
from .models import MainTable

def Main_list(request):
    Table = MainTable.objects.all()
    return render(request, 'test.html', {'posts': Table})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(MainTable,
                                   status='published',
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    return render(request,'list.html', {'post': post})
