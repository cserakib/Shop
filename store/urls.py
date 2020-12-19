from django.urls import path
from .import views
urlpatterns =[
    path('',views.Index.as_view(), name='home'),
    path('singup', views.singup, name='singup'),
    path('login', views.Login.as_view(), name='login'),
]