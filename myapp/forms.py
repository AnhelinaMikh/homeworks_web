from django import forms
from django.core.exceptions import ValidationError

from django.forms import ModelForm
from .models import Author, Book

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
