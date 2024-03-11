import time

from celery import shared_task
from django.db.models import F

from books.models import VisitCounter


@shared_task()
def increase_visitors_shared():
    time.sleep(5)
    VisitCounter.objects.filter(pk=1).update(visitors=F('visitors') + 1)
    time.sleep(5)

