from . import views
from django.urls import path, re_path

app_name = "MainPages"
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('modules', views.modules, name='modules'),
    path('professors', views.professors, name='professors'),
    path('rate', views.rate, name='rate'),
    path('register', views.register, name='register'),
]