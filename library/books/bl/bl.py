from books.models import VisitCounter
import time


def increase_visitors():
    time.sleep(3)
    visit = VisitCounter.objects.first()
    if not visit:
        visit = VisitCounter.objects.create(visitors=0)

    visit.visitors += 1
    visit.save()
