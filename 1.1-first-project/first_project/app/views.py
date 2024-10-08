from django.http import HttpResponse
from django.shortcuts import render, reverse

import datetime, os




def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    template_name = 'app/time.html'
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return render(request, template_name, context={"current_time": current_time})


def workdir_view(request):
    dir_list = os.listdir(os.getcwd())
    template_name = 'app/dir_list.html'
    return(render(request, template_name, context={'dir_list': dir_list}))
