from __future__ import absolute_import, unicode_literals
from celery import shared_task
from github import Github
from django.conf import settings

from .models import Commit

g = Github(settings.GITHUB_TOKEN)

@shared_task
def fetch_commits():
    repo = g.get_repo('nodejs/node')
    for commit in repo.get_commits()[:25]:
        Commit.objects.get_or_create(
            sha=commit.sha,
            name=commit.commit.author.name,
            email=commit.commit.author.email,
        )
