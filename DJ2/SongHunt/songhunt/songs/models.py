from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    title = models.CharField(max_length=255)
    band = models.CharField(max_length=50, default='XXXX')
    date_added = models.DateTimeField()
    votes_total = models.IntegerField(default =1)
    notes = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def dated_added_pretty(self):
        return self.date_added.strftime('%b %e %Y')


