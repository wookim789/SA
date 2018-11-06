from django.conf import settings
from django.conf.urls import include  # For django versions before 2.0
from django.urls import path  # For django versions from 2.0 and up
from onePage import views
from onePage import login

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
        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] 



