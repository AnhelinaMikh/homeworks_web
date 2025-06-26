from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Author, Book, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Article

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']



class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'text', 'genre', 'topics']


class MyForm(forms.Form):
    nickname = forms.CharField(label='My nickname', max_length=100)
    age = forms.IntegerField(label='My age')

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if nickname.lower() == 'admin':
            raise ValidationError('Nickname "admin" is not allowed.')
        return nickname


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'title', 'birth_date']

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'authors']


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required field')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user