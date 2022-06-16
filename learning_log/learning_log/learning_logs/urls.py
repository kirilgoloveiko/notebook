from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Страница со списком всех тем
    path('topics/', views.topics, name='topics'),
    # Страница с подробной информацией по отдельной теме
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Страница для добавления новой ТЕМЫ
    path('new_topic/', views.new_topic, name='new_topic'),
    # Страница для добавления новых ЗАПИСЕЙ
    path('new_record/<int:topic_id>/', views.new_record, name='new_record'),
    # Страница для редактирования ранее добаленных записей
    path('edit_record/<int:record_id>/', views.edit_record, name='edit_record')
]