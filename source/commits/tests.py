from urllib2 import urlopen
import json

from django.test import TestCase

from .tasks import get_latest_commit
from .models import Commits


class TasksMethodTests(TestCase):

    def test_get_latest_commit(self):
        """
        test_get_latest_commit - checking get_latest_commit saved only new commits
        """
        error = ''
        list = get_latest_commit()
        for el in list:
            sha = el['sha']
            try:
                if not Commits.objects.get(sha=sha):
                    error = 'object not exist'
            except Exception as ex:
                    error = 'there are duplicates'
        self.assertEqual(error, '')