from django.conf import settings
from django.conf.urls import include  # For django versions before 2.0
from django.urls import path  # For django versions from 2.0 and up
from onePage import views
from onePage import login
from onePage import signUp
from onePage import mainPageTeam

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('', views.index),
        path('onePage/getMemberId/', views.getMemberId),
        path('onePage/loadCalendar/', views.loadCalendar),
        path('onePage/selectCalendar/', views.selectCalendar),
        path('onePage/fixcal/', views.fixcal),
        path('onePage/login/', login.login),
        path('onePage/checkId/', signUp.checkId),
        path('onePage/signUp/', signUp.signUp),
        path('onePage/loadTeamNameList/', mainPageTeam.loadTeamNameList),
        path('onePage/checkTeamName/', mainPageTeam.checkTeamName),
        path('onePage/makeTeam/', mainPageTeam.makeTeam),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] 



