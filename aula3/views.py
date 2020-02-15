from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone


def index(request):
    html = '<h1>Bem vindo</h1>'
    response = HttpResponse(html)
    response['ultimo_acesso'] = timezone.localtime(timezone.now())
    return response


def setacookie(request):
    response = HttpResponse()
    response.set_cookie('my_name', value='Marcel')
    return response


def redireciona(request):
    return HttpResponseRedirect('https://uol.com.br')
