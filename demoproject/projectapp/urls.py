from django.urls import path

from projectapp import views

urlpatterns = [
    path('',views.page,name="index.html"),
    path('register',views.register,name='register'),
    path('login',views.login, name='login'),
    path('logout',views.logout,name='logout')
]
