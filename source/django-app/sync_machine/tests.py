from django.test import Client
from django.test import TestCase
import json

from sync_machine.models import Contributor, Commit


class AuthTest(TestCase):
    def setUp(self):
        Commit.data_loader.run()

    def test_api_authors(self):
        """
        Should test API route: /api/authors
        :return:
        """
        count_authors = Contributor.objects.all().count()

        response = Client().get('/api/authors/')
        content = json.loads(response.content.decode("utf-8"))
        result = content.get('result')

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(result)
        self.assertEqual(count_authors, len(result))

    def test_api_commits_author(self):
        """
        Should test API route: /api/commits/author/(?P<author_id>[0-9]+)
        :return:
        """
        author = Contributor.objects.all().first()
        commit_author_count = Commit.objects.filter(author_id=author.id).count()

        response = Client().get('/api/commits/author/' + str(author.id) + '/')
        content = json.loads(response.content.decode("utf-8"))
        result = content.get('result')

        self.assertIsNotNone(author)
        self.assertGreater(commit_author_count, 0)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(result), commit_author_count)

    def test_api_commit_status(self):
        """
        Should test API route: /api/commit/(?P<commit_id>[0-9]+)/(?P<status>(r|u)+)
        :return:
        """
        author = Contributor.objects.all().first()
        commit = Commit.objects.filter(author_id=author.id).first()

        self.assertIsNotNone(commit)
        self.assertEqual(commit.status, 'U')

        response = Client().get('/api/commit/' + str(commit.id) + '/' + 'R' + '/')
        self.assertEqual(response.status_code, 200)

        commit.refresh_from_db()
        self.assertEqual(commit.status, 'R')
