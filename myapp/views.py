from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, time
from .forms import MyForm
from django.shortcuts import redirect
from .forms import AuthorForm
from django.views import View
from django.http import Http404

import datetime

def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-page')  
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})



class FormView(View):
    def get(self, request):
        form = MyForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'form_was_valid.html')
        return render(request, 'form.html', {'form': form})



class MyClass:
    string = ''

    def __init__(self, s):
        self.string = s

def home(request):
    return HttpResponse("Это главная страница")

def about(request):
    return HttpResponse("Это страница 'О нас'")

def contacts(request):
    return HttpResponse("Это страница с контактами")

def index(request):
    context = {
        "now": datetime.now(),
        "value": time(14, 30),
        "not_exist": None,
        "my_str": "hello world",
        "my_list": ["one", "two", "three"],
    }
    return render(request, 'index.html', context)


def first(request):
    return render(request, 'first.html')

def my_feed(request):
    return HttpResponse("Страница с лентой пользователя по его подпискам")

def article_detail(request, article_id):
    return HttpResponse(f"Статья с ID {article_id}")

def article_comment(request, article_id):
    return HttpResponse(f"Добавление комментария к статье с ID {article_id}")

def article_update(request, article_id):
    return HttpResponse(f"Редактирование статьи с ID {article_id}")

def article_delete(request, article_id):
    return HttpResponse(f"Удаление статьи с ID {article_id}")

def create_article(request):
    return HttpResponse("Создание новой статьи")

def topic_list(request):
    return HttpResponse("Список всех тем")

def topic_articles(request, topic_id):
    return HttpResponse(f"Статьи по теме ID {topic_id}")

def topic_subscribe(request, topic_id):
    return HttpResponse(f"Подписка на тему ID {topic_id}")

def topic_unsubscribe(request, topic_id):
    return HttpResponse(f"Отписка от темы ID {topic_id}")

def profile_view(request):
    return HttpResponse("Профиль пользователя и подписки")

def register_view(request):
    return HttpResponse("Регистрация нового пользователя")

def login_view(request):
    return HttpResponse("Вход пользователя")

def logout_view(request):
    return HttpResponse("Выход пользователя")

def set_password(request):
    return HttpResponse("Смена пароля")

def articles_by_date(request, year, month):
    try:
        datetime.datetime(year, month, 1)
    except ValueError:
        raise Http404("Неправильная дата")
    return HttpResponse(f"Статьи за {month:02}/{year}")