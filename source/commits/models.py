from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Commits(models.Model):
    class Meta():
        db_table = 'commits'


    sha = models.CharField(max_length=200, default='')
    author = models.CharField(max_length=200, blank=True, default='')
    pub_date = models.DateTimeField()
    text = models.TextField()
    read_status = models.BooleanField(default=False)

