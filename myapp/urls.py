from django.urls import path
from .views import (
    IndexView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView,
    TopicDetailView, FormView, register_view, login_view, logout_view, set_password,
    my_feed, topic_list, topic_subscribe, topic_unsubscribe, profile_view,
    about, contacts, first, create_author, articles_by_date
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('first/', first, name='first'),
    path('create-author/', create_author, name='create-author'),
    path('form-url/', FormView.as_view(), name='form-view'),

    path('my-feed/', my_feed, name='my-feed'),
    path('create/', ArticleCreateView.as_view(), name='create-article'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('<int:year>/<int:month>/', articles_by_date, name='articles-by-date'),

    path('topics/', topic_list, name='topic-list'),
    path('topics/<int:pk>/', TopicDetailView.as_view(), name='topic-articles'),
    path('topic/<int:topic_id>/subscribe/', topic_subscribe, name='topic-subscribe'),
    path('topic/<int:topic_id>/unsubscribe/', topic_unsubscribe, name='topic-unsubscribe'),

    path('profile/', profile_view, name='profile'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('set-password/', set_password, name='set-password'),
]
