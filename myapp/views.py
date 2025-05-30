from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime, time
from .forms import MyForm
from django.shortcuts import redirect
from .forms import AuthorForm


def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success-page')  # замените на вашу страницу
    else:
        form = AuthorForm()
    return render(request, 'author_form.html', {'form': form})

# to lesson 23
def form_view(request):
    # name = request.GET.get("my_name")
    # return render(request, "form.html", {"name": name}) 
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            return render(request, 'form_was_valid.html')
    else:
        form = MyForm()

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

# def index(request):
#     my_num = 33
#     my_str = 'some string'
#     my_dict = {"some_key": "some_value"}
#     my_list = ['list_first_item', 'list_second_item', 'list_third_item']
#     my_set = {'set_first_item', 'set_second_item', 'set_third_item'}
#     my_tuple = ('tuple_first_item', 'tuple_second_item', 'tuple_third_item')
#     my_class = MyClass('class string')
#     return render(request, 'index.html', {
#         'my_num': my_num,
#         'my_str': my_str,
#         'my_dict': my_dict,
#         'my_list': my_list,
#         'my_set': my_set,
#         'my_tuple': my_tuple,
#         'my_class': my_class,
#         'display_num': True,
#         'now': datetime.now()
#     })
# 1st version

# def first(request):
#     return HttpResponse("Это страница First")

def first(request):
    return render(request, 'first.html')