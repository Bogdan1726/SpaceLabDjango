from django.urls import path
from .views import *

urlpatterns = [
    path('', test_redis),
    path('test-celery/', test_celery)
]
