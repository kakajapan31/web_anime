from django.urls import path
from web_film import  views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Film_list_view.as_view(), name='index'),
    path('help/', views.Help.as_view(), name='help'),
    path('about_me/', views.About_me.as_view(), name='about_me'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('my_account/', views.My_account.as_view(), name='my_account'),
    path('logout/', views.logout, name='logout'),
    path('change_password/',  views.Change_password.as_view(), name='change_password'),
    path('forgot_password/', views.Forgot_password.as_view(), name='forgot_password'),
    path('question/<int:pk>/', views.Question_view.as_view(), name='question'),
    path('film/<int:pk>/', views.Film_view.as_view(), name='film'),
    path('author/<int:pk>/', views.Author_view.as_view(), name='author'),
    path('actor/<int:pk>/', views.Actor_view.as_view(), name='actor'),
    path('genre/<int:pk>/', views.Genre_view.as_view(), name='genre'),
]