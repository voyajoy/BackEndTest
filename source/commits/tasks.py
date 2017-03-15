from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from django.utils import timezone

from .models import Commits
from urllib2 import urlopen
from dateutil.parser import parse

import json

logger = get_task_logger(__name__)


@periodic_task(ignore_result=True, run_every=(crontab(hour="*", minute=timezone.now().minute+1, day_of_week="*")))
def get_latest_commit(owner='nodejs', repo='node'):
    logger.info("Start task")
    url = 'https://api.github.com/repos/{owner}/{repo}/commits'.format(owner=owner, repo=repo)
    response = urlopen(url).read()
    data = json.loads(response.decode('UTF-8'))
    list = data[:25]
    for el in list:
        sha = el['sha']
        name = el['commit']['author']['name']
        msg = el['commit']['message'].encode('ascii','ignore')
        date = parse(el['commit']['author']['date'])
        try:
            if not Commits.objects.filter(sha=sha):
                comment = Commits(author=name, text=msg, pub_date=date, read_status=False, sha=sha)
                comment.save()
                logger.info("Get!!!")
        except Exception as ex:
            print('ex is: {}'.format(ex))
    logger.info("End task success!!!")
    return list
    