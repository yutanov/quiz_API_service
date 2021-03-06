from django.urls import path
from que import views

urlpatterns = [
    path('', views.index, name='home'),
    path('last_question', views.view_last_obj, name='last'),
    path('quiz/', views.QuizList.as_view()),
    path('quiz/<int:pk>/', views.QuizDetail.as_view()),
    path('questions_num', views.get_num_of_questions, name='form'),
    path('q', views.get_q),
    path('last', views.get_last_obj),
]
