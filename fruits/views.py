from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import *

menu = [
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Услуги', 'url_name': 'services'},
    {'title': 'Решить задачу', 'url_name': 'task'},
]

posts = Fruits.objects.all()


def index(request):
    context = {'posts': posts,
               'menu': menu,
               'title': 'Главная страница',
               }
    return render(request, 'fruits/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О нас',
        'me': {
            'name': 'Першина Ольга Николаевна',
            'phone': '+79993764580',
            'mail': 'onpershina@edu.hse.ru',
            'img': 'https://images.wallpaperscraft.ru/image/single/domik_zima_sneg_134709_1280x720.jpg'
        },
        'program': {
            'name': 'Фундаментальная и прикладная лингвистика',
            'description': 'Программа имеет два направления подготовки: мы готовим специалистов в области '
                           'компьютерной лингвистики (разработчики электронных лингвистических систем) и специалистов '
                           'в области прикладного и теоретического языкознания (преподаватели иностранных языков, '
                           'преподаватели русского как иностранного, переводчики, судебные эксперты-лингвисты).',
            'leader': {
                'name': 'Климова Маргарита Андреевна',
                'mail': 'mfokina@hse.ru',
                'img': 'https://www.hse.ru/org/persons/cimage/91748436'
            },
            'manager': {
                'name': 'Суравенкова Анна Андреевна',
                'mail': 'asuravenkova@hse.ru',
                'img': 'https://www.hse.ru/org/persons/cimage/208526887'
            }
        },
        'student1': {
            'name': 'Водопьянова Юлия',
            'phone': '+79999999999',
            'mail': 'yuevodopyanova@edu.hse.ru',
            'img': 'https://images.wallpaperscraft.ru/image/single/kot_lezhat_milyj_56210_1280x720.jpg'
        },
        'student2': {
            'name': 'Тасенко Ольга',
            'phone': '+79999999999',
            'mail': 'oatasenko@edu.hse.ru',
            'img': 'https://images.wallpaperscraft.ru/image/single/kot_morda_son_51097_1280x720.jpg'
        },
    }
    return render(request, 'fruits/about.html', context)


def show_post(request, post_id):
    fruit = get_object_or_404(Fruits, pk=post_id)
    context = {
        'fruit': fruit,
        'menu': menu,
        'title': fruit.title,
    }
    return render(request, 'fruits/post.html', context)


def task(request):
    information = {
        'menu': menu,
        'title': 'Решение задачи',
    }
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        if all(map(lambda x: is_integer(x), [a, b, c])):
            try:
                a = float(a)
                b = float(b)
                c = float(c)
                if a < b < c:
                    inequality = 'A < B < C'
                elif a < b > c:
                    inequality = 'A < B > C'
                else:
                    inequality = 'Не выполняется ни одно из указанных неравенств'

                return render(request, 'fruits/answer.html', {'inequality': inequality, **information})
            except ValueError:
                return render(request, 'fruits/error_task.html', context=information)
        else:
            return render(request, 'fruits/error_task.html', context=information)
    else:
        return render(request, 'fruits/task.html', context=information)


def is_integer(value):
    try:
        int(value)
        return False
    except ValueError:
        return True


def sets_of_fruits(request):
    context = {
        'menu': menu,
        'title': 'Наборы фруктов'
    }
    return render(request, 'fruits/sets_of_fruits.html', context=context)


def services(request):
    context = {
        'menu': menu,
        'title': 'Наборы фруктов'
    }
    return render(request, 'fruits/services.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена</h1>')
