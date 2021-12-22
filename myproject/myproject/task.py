from time import sleep
from myproject.celery import app
from django.core.mail import send_mail


@app.task
def send_email():
    sleep(10)
    user_email = 'bogdan24ro@gmail.com'
    send_mail('Spam',
              'Hello World',
              'okcdnipro@gmail.com',
              [user_email],
              fail_silently=False)

