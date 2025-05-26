from django.urls import path
from .views import home, about, contacts, index, first  # добавили first

urlpatterns = [
    path('', index, name='index'),       # Главная страница
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('first/', first, name='first'),  # <- Вот здесь добавлен маршрут с именем 'first'
]


#http://127.0.0.1:8000/

#http://127.0.0.1:8000/about/

#http://127.0.0.1:8000/contacts/



