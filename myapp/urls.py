from django.urls import path
from .views import home, about, contacts  # Убедись, что эти функции есть в views.py

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
]

#http://127.0.0.1:8000/

#http://127.0.0.1:8000/about/

#http://127.0.0.1:8000/contacts/