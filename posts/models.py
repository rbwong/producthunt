from datetime import datetime, timedelta, time

from django.db import models

from authentication.models import Account


class TodayPostManager(models.Manager):

    def get_queryset(self):
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        return super(TodayPostManager, self).get_queryset().filter(created_at__range=[today, tomorrow])


class Post(models.Model):
    author = models.ForeignKey(Account)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    today_objects = TodayPostManager()

    def __unicode__(self):
        return '{0}'.format(self.content)
