from django.urls import path
from .views import (
    index, about, contacts, first, create_author, FormView, article_detail,
    article_comment, article_update, article_delete, create_article, my_feed,
    topic_list, topic_articles, topic_subscribe, topic_unsubscribe, profile_view,
    register_view, login_view, logout_view, set_password, articles_by_date
)





urlpatterns = [
    
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('first/', first, name='first'),
    path('create-author/', create_author, name='create-author'),
    path('form-url/', FormView.as_view(), name='form-view'),

    # ДОБАВЛЕННЫЕ ДЛЯ ДЗ:
    path('', index, name='index'), #
    path('my-feed/', my_feed, name='my-feed'), #
    path('create/', create_article, name='create-article'), #
    path('<int:year>/<int:month>/', articles_by_date, name='articles-by-date'), #
    path('<int:article_id>/', article_detail, name='article-detail'), #
    path('<int:article_id>/comment/', article_comment, name='article-comment'), #
    path('<int:article_id>/update/', article_update, name='article-update'), #
    path('<int:article_id>/delete/', article_delete, name='article-delete'), #

    path('topics/', topic_list, name='topic-list'),
    path('topics/<int:topic_id>/', topic_articles, name='topic-articles'), #
    path('topics/<int:topic_id>/subscribe/', topic_subscribe, name='topic-subscribe'),
    path('topics/<int:topic_id>/unsubscribe/', topic_unsubscribe, name='topic-unsubscribe'),

    path('profile/', profile_view, name='profile'), #
    path('register/', register_view, name='register'), #
    path('set-password/', set_password, name='set-password'), #
    path('login/', login_view, name='login'), #
    path('logout/', logout_view, name='logout'), #

    
]





