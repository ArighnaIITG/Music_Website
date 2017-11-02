from django.conf.urls import url
from . import views

app_name = 'music' #Namespace..to indicate that detail is a part of music app

urlpatterns = [
    #music/
    url(r'^$',views.index, name='index'),
    
    #music/<album_id>
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]