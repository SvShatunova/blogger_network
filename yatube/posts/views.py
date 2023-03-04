from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница блога')



def group_list(request, slug):
    return HttpResponse('Выберите категорию')
