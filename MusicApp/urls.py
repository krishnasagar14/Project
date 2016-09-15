__author__ = 'krishnasagar'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Music_track),
    url(r'^tracks/$', views.Music_track),
    url(r'^tracks/(?P<page>[0-9]+)/$', views.Music_track),
    url(r'^addTrack/$', views.Add_Track),
    url(r'^editTrack/(?P<id>[0-9]+)/$',views.Edit_Track),

    url(r'^genres/$', views.Track_Genre),
    url(r'^genres/(?P<page>[0-9]+)/$', views.Track_Genre),
    url(r'^addGenre/$', views.Add_Genre),
    url(r'^editGenre/(?P<id>[0-9]+)/$',views.Edit_Genre),
]