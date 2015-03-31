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
    name = models.CharField(max_length=80)
    tagline = models.CharField(max_length=140, blank=True)
    day = models.CharField(max_length=10, blank=True)
    votes_count = models.IntegerField(default=0, blank=True)
    comments_count = models.IntegerField(default=0, blank=True)
    discussion_url = models.URLField(blank=True)
    redirect_url = models.URLField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    today_objects = TodayPostManager()

    def __unicode__(self):
        return '{0}'.format(self.name)

    def save(self, *args, **kwargs):
        self.day = datetime.strftime(datetime.now().date(), '%m-%d-%Y')
        super(Post, self).save(*args, **kwargs)
