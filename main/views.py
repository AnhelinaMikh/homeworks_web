# mysite/myapp/views.py
from django.http import HttpResponse, HttpRequest


# Поздравляю, это ваш первый контроллер, который может принять запрос и отдать ответ с текстом, больше ничего
def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hey! It's your main view!!")