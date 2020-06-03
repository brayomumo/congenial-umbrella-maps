from django.db import models
from django.utils import timezone

# Create your models here.
class TweetObject(models.Model):
    date = models.CharField(max_length=256)
    text = models.CharField(max_length=256)
    polarity = models.FloatField()
    subjectivity = models.FloatField()
    mentions = models.CharField(max_length = 256, blank=True)
    hashtag = models.CharField(max_length = 256, blank=True)
    location = models.CharField(max_length = 256, blank=True)
    route = models.CharField(max_length = 256, blank=True,null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    conditions = models.CharField(max_length = 256, blank=True,null=True)
    created_date = models.DateTimeField('date Created', default =timezone.now)

    def __str__(self):
        return self.hashtag