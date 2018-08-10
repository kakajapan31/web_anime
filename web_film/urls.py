from django.urls import path
from web_film import  views

urlpatterns = [
    path('', views.Film_list_view.as_view(), name='index'),
    path('help/', views.Help.as_view(), name='help'),
    path('my_account/', views.My_account.as_view(), name='my_account'),

    path('about_me/', views.About_me.as_view(), name='about_me'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.logout, name='logout'),
    path('change_password/',  views.Change_password.as_view(), name='change_password'),
    path('forgot_password/', views.Forgot_password.as_view(), name='forgot_password'),

    path('question/<int:pk>/', views.Question_view.as_view(), name='question'),
    path('film/<int:pk>/', views.Film_view.as_view(), name='film'),
    path('author/<int:pk>/', views.Author_view.as_view(), name='author'),
    path('actor/<int:pk>/', views.Actor_view.as_view(), name='actor'),
    path('genre/<int:pk>/', views.Genre_view.as_view(), name='genre'),
    path('film_view/<int:pk>', views.Film_page_view.as_view(), name='film_page'),

    path('api/question/', views.Question_List_view.as_view(), name='api_list_question'),
    path('api/question/<int:pk>/', views.Question_Detail_view.as_view(), name='api_detail_question'),
    path('api/question/<int:pk>/choices/', views.Choice_List_of_Question.as_view(), name='api_detail_answer_of_question'),
    path('api/question/<int:pk>/choices/<int:choice_pk>/', views.Choice_Detail_of_Question.as_view(), name='api_detail_anwser_i_of_question_j'),

    path('api/film/', views.Film_List_view.as_view(), name='api_list_film'),
    path('api/film/<int:pk>/', views.Film_Detail_view.as_view(), name='api_detail_film'),
    path('api/author/', views.Author_List_view.as_view(), name='api_list_author'),
    path('api/author/<int:pk>/', views.Author_Detail_view.as_view(), name='api_detail_author'),
    path('api/actor/', views.Actor_List_view.as_view(), name='api_list_actor'),
    path('api/actor/<int:pk>/', views.Actor_Detail_view.as_view(), name='api_detail_actor'),
    path('api/genre/', views.Genre_List_view.as_view(), name='api_list_genre'),
    path('api/genre/<int:pk>/', views.Genre_Detail_view.as_view(), name='api_detail_genre'),
    path('api/film/<int:pk>/list/', views.Fitm_th_view.as_view(), name='api_film_list'),
    path('api/film/<int:pk>/list/<int:film_pk>', views.Film_th_Detail_of_Film.as_view(), name='api_detail_filmth_i_of_film_j'),
]