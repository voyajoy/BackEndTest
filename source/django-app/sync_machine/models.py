from django.db import models
from urllib import request
import json


class Contributor(models.Model):
    name = models.CharField(blank=False, max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class CommitDataLoader(models.Manager):
    def run(self):
        path = 'https://api.github.com/repos/nodejs/node/commits'
        f = request.urlopen(path)
        response = f.read().decode('utf-8')
        commits = json.loads(response)
        for commit in commits:
            sha = commit.get('sha')
            message = commit['commit']['message']

            author_email = commit['commit']['author']['email']
            author_name = commit['commit']['author']['name']
            author, created = Contributor.objects.get_or_create(
                email=author_email,
                name=author_name)

            Commit.objects.get_or_create(sha=sha,
                                         defaults={
                                             'author': author,
                                             'message': message
                                         })


class Commit(models.Model):
    STATUS_TYPE = (
        ('R', 'read'),
        ('U', 'unread')
    )

    sha = models.CharField(blank=False, max_length=40)
    message = models.TextField()
    author = models.ForeignKey(Contributor)
    status = models.CharField(blank=False, max_length=1, default='U', choices=STATUS_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    data_loader = CommitDataLoader()
    objects = models.Manager()
