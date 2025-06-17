# models.py
from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):  
    name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/')
    topics = models.ManyToManyField('Topic', blank=True)

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

class Topic(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(User, related_name="subscribed_topics", blank=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=100)  # или title
    text = models.TextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='articles')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    genre = models.IntegerField(choices=GENRE_CHOICES, default=1)

    def __str__(self):
        return self.name

    topics = models.ManyToManyField(Topic, blank=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text} by {self.user.username}"



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"By user {self.user.username} to article {self.article.id}"
    

    #lection 23
TITLE_CHOICES = [
    ('MR', 'Mr'),
    ('MRS', 'Mrs'),
    ('MS', 'Ms'),
    ('MISS', 'Miss'),
    ('DR', 'Dr'),
]



class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=10, choices=TITLE_CHOICES)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_title_display()} {self.name}"

class Book(models.Model):
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)