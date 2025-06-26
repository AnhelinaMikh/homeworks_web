# models.py
from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)

class Profile(models.Model):  # ДОЛЖЕН быть на том же уровне, что и Article
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')

    def __str__(self):
        return self.name

# lection 22
from django.utils import timezone
from django.utils.translation import gettext as _

GENRE_CHOICES = (
    (1, _("Not selected")),
    (2, _("Comedy")),
    (3, _("Action")),
    (4, _("Beauty")),
    (5, _("Other"))
)


# class Author(models.Model):
#     pseudonym = models.CharField(max_length=120, blank=True, null=True)
#     name = models.CharField(max_length=120)

#     def __str__(self):
#         return self.name


# class Article(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='articles')
#     text = models.TextField(max_length=10000, null=True)
#     created_at = models.DateTimeField(default=timezone.now)
#     updated_at = models.DateTimeField(default=timezone.now)
#     genre = models.IntegerField(choices=GENRE_CHOICES, default=1)

#     def __str__(self):
#         return f"Author - {self.author.name}, genre - {self.genre}, id - {self.id}"


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('myapp.Comment', null=True, blank=True, on_delete=models.DO_NOTHING, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.text} by {self.user.username}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"By user {self.user.username} to article {self.article.id}"
    

    #lection 23
TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)