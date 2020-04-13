from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('about', views.about, name='about'),
    path('view_changelogs', views.view_changelogs, name='view_changelogs'),
    path('view_sounddefs', views.view_sounddefs, name='view_sounddefs'),
    path('changelogs/download/<str:filename>', views.download, {'filetype': 'changelogs'}),
    path('sounddefs/download/<str:filename>', views.download, {'filetype': 'sound_defs'})
]
