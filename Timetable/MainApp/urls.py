from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.Main_list, name='Main_list'),
    url(r'^$',
        views.post_detail,
        name='post_detail'),
]
