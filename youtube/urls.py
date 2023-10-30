from django.urls import path
from youtube import views

urlpatterns = [
    path('', views.index, name='home'), # path(/abc , views.abc_function , abc.html)
    path('huongdan/', views.huongdan, name='huongdan'),
    path('about/', views.about, name='about')
]
