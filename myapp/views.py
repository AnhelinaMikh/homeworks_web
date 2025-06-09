from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, time
from .forms import MyForm
from django.shortcuts import redirect
from .forms import AuthorForm
from django.views import View
from django.http import Http404


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
    return HttpResponse("Page with a user's feed of their subscriptions")

def article_detail(request, article_id):
    return HttpResponse(f"Article with ID {article_id}")

def article_comment(request, article_id):
    return HttpResponse(f"Adding a comment to an article with ID {article_id}")

def article_update(request, article_id):
    return HttpResponse(f"Editing an article with an ID {article_id}")

def article_delete(request, article_id):
    return HttpResponse(f"Deleting an article with ID{article_id}")

def create_article(request):
    return HttpResponse("Creating a new article")

def topic_list(request):
    return HttpResponse("List of all topics")

def topic_articles(request, topic_id):
    return HttpResponse(f"Articles on the topic ID {topic_id}")

def topic_subscribe(request, topic_id):
    return HttpResponse(f"Topic Subscription ID {topic_id}")

def topic_unsubscribe(request, topic_id):
    return HttpResponse(f"Unsubscribe from the topic ID {topic_id}")

def profile_view(request):
    return HttpResponse("User profile and subscriptions")

def register_view(request):
    return HttpResponse("New User Registration")

def login_view(request):
    return HttpResponse("User Login")

def logout_view(request):
    return HttpResponse("User Logout")

def set_password(request):
    return HttpResponse("Change password")

def articles_by_date(request, year, month):
    try:
        datetime.datetime(year, month, 1)
    except ValueError:
        raise Http404("Incorrect date")
    return HttpResponse(f"Статьи за {month:02}/{year}")