from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.cache import cache
from myproject.task import *
from django.contrib import messages


# Create your views here.


def test_redis(request):
    if 'users' in cache:
        users = cache.get('users')
        return render(request, 'home/index.html', {'users': users})
    else:
        users = User.objects.all().count()
        cache.set('users', users, timeout=10)
        return render(request, 'home/index.html', {'users': users})


def test_celery(request):
    if request.method == 'POST':
        send_email.delay()
        messages.success(request, 'Вы подписались на рассылку новостей')
    return render(request, 'home/celery.html')
