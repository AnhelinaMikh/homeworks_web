from datetime import datetime
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin

from .forms import MyForm, AuthorForm, RegisterForm, CommentForm, ArticleForm
from .models import Article, Topic, Comment


# --- Auth views ---
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('index')
        messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

def set_password(request):
    return HttpResponse("Change password (to be implemented)")


# --- Main page ---
class IndexView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    ordering = ['-created_at']


def about(request):
    return HttpResponse("About page")

def contacts(request):
    return HttpResponse("Contacts page")

def first(request):
    return render(request, 'first.html')


# --- Form example ---
class FormView(View):
    def get(self, request):
        return render(request, 'form.html', {'form': MyForm()})

    def post(self, request):
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'form_was_valid.html')
        return render(request, 'form.html', {'form': form})


# --- Author creation ---
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})


# --- My Feed ---
@login_required
def my_feed(request):
    topics = request.user.subscribed_topics.all()
    articles = Article.objects.filter(topics__in=topics).distinct().order_by('-created_at')
    return render(request, 'my_feed.html', {'articles': articles, 'topics': topics})


# --- Articles ---
class ArticleDetailView(FormMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'article'
    form_class = CommentForm

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comment_set.all()
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = self.object
            comment.author = request.user
            comment.save()
            return redirect(self.get_success_url())
        return self.form_invalid(form)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('index')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_confirm_delete.html'
    success_url = reverse_lazy('index')


# --- Topics ---
class TopicDetailView(DetailView):
    model = Topic
    template_name = 'topic_articles.html'
    context_object_name = 'topic'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = self.object.article_set.order_by('-created_at')
        return context


def topic_list(request):
    return render(request, 'topic_list.html', {'topics': Topic.objects.all()})

@login_required
def topic_subscribe(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    topic.subscribers.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def topic_unsubscribe(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    topic.subscribers.remove(request.user)
    return redirect(request.META.get('HTTP_REFERER', '/'))


def profile_view(request):
    return HttpResponse("User profile (to be implemented)")


def articles_by_date(request, year, month):
    try:
        datetime(year, month, 1)
    except ValueError:
        raise Http404("Invalid date")
    articles = Article.objects.filter(created_at__year=year, created_at__month=month).order_by('-created_at')
    return render(request, 'articles_by_date.html', {'articles': articles, 'year': year, 'month': month})
