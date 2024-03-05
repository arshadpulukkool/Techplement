from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('operation',views.operations,name='op'),
    path('notlogged',views.AnonymousUser,name='anonymous'),
    path('login',views.loginform,name='login'),
    path('reg',views.register,name='reg'),
    path('del/<int:id>', views.delete),
    path('logout',views.logout_view,name='logout')
]