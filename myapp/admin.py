from django.contrib import admin
from .models import Article, Comment, Like, Author, Book, Profile, Topic

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Topic)
