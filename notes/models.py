from django.db import models
from django.core.urlresolvers import reverse
from datetime import datetime


class Note(models.Model):
    note_title = models.CharField(max_length=250)
    brief = models.CharField(max_length=100)
    body = models.CharField(max_length=10000)
    date = models.DateTimeField(default=datetime.now)
    note_logo = models.FileField(blank= True, null=True)

    def get_absolute_url(self):
        return reverse('notes:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.note_title






