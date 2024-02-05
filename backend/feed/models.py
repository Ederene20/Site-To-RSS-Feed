from django.db import models

from abstract.models import AbstractModel, AbstractManager
from user.models import User


class FeedManager(AbstractManager):
    pass


class Feed(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    global_search_pattern = models.CharField(max_length=200)
    search_pattern = models.CharField(max_length=200)
    feed_title = models.CharField(max_length=50)
    feed_link = models.CharField(max_length=200)
    feed_description = models.CharField(max_length=200)
    item_title_template = models.CharField(max_length=12)
    item_link_template = models.CharField(max_length=12)
    item_content_template = models.CharField(max_length=12)

    objects = FeedManager()
