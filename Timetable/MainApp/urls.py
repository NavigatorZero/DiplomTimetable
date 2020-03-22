from django.conf.urls import url
from . import views

urlpatterns = [
    # post views

    url('', views.Main_list, name='Main_list'),
]
