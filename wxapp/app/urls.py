# chat/urls.py
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^quests/$', views.QuestList.as_view(), name='questlist'),
    url(r'^quests/(?P<pk>[0-9]+)/$', views.QuestDetail.as_view(), name='questdetail'),
    url(r'^sign/$', views.SignList.as_view(), name='signlist'),
    url(r'^sign/(?P<pk>[0-9]+)/$', views.SignDetail.as_view(), name='signdetail'),
    url(r'^img/$', views.ImgList.as_view(), name='imglist'),
    url(r'^img/(?P<pk>[0-9]+)/$', views.ImgDetail.as_view(), name='imgdetail'),
    url(r'^treasure/$', views.TreasureList.as_view(), name='treasurelist'),
    url(r'^treasure/(?P<pk>[0-9]+)/$', views.TreasureDetail.as_view(), name='treasuredetail'),
    url(r'^log/$', views.LogList.as_view(), name='loglist'),
    url(r'^log/(?P<pk>[0-9]+)/$', views.LogDetail.as_view(), name='logdetail'),
    url(r'^user/$', views.UserList.as_view(), name='userlist'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='userdetail'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
urlpatterns = format_suffix_patterns(urlpatterns)