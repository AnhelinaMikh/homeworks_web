from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, time
from .forms import MyForm
from django.shortcuts import redirect
from .forms import AuthorForm
from django.views import View
from django.http import Http404
from .models import Article, Topic, Comment
from django.db.models import Q


def article_list(request):
    articles = Article.objects.all().order_by('-created_at')  
    context = {
        'articles': articles,
    }
    return render(request, 'article_list.html', context)

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
    articles = Article.objects.order_by('-created_at')
    return render(request, 'index.html', {'articles': articles})


def first(request):
    return render(request, 'first.html')


def my_feed(request):
   
    interesting_topics = ['Sport', 'Film']
    
    articles = Article.objects.filter(
        topics__name__in=interesting_topics
    ).distinct().order_by('-created_at')

    return render(request, 'my_feed.html', {'articles': articles, 'topics': interesting_topics})

def article_detail(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article not found")

    comments = Comment.objects.filter(article=article)

    return render(request, 'article_detail.html', {
        'article': article,
        'comments': comments
    })

def article_comment(request, article_id):
    return HttpResponse(f"Adding a comment to an article with ID {article_id}")

def article_update(request, article_id):
    return HttpResponse(f"Editing an article with an ID {article_id}")

def article_delete(request, article_id):
    return HttpResponse(f"Deleting an article with ID{article_id}")

def create_article(request):
    return HttpResponse("Creating a new article")

def topic_list(request):
    topics = Topic.objects.all()
    return render(request, 'topic_list.html', {'topics': topics})

def topic_articles(request, topic_id):
    try:
        topic = Topic.objects.get(pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic not found")

    articles = topic.article_set.order_by('-created_at')
    return render(request, 'topic_articles.html', {
        'topic': topic,
        'articles': articles
    })


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
        date = datetime(year, month, 1)
    except ValueError:
        raise Http404("Incorrect date")

    articles = Article.objects.filter(
        created_at__year=year,
        created_at__month=month
    ).order_by('-created_at')

    return render(request, 'articles_by_date.html', {
        'articles': articles,
        'year': year,
        'month': month
    })
