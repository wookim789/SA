
from django.urls import path
from onePage import views

urlpatterns = [
    #   path('admin/', admin.site.urls),
    path('', views.index),
    path('ajax/getMemberId/', views.getMemberId),
]
