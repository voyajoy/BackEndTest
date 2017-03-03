import json

from django.test import TestCase, Client
from .models import Commit

class APITests(TestCase):
    def setUp(self):
        self.c = Client()

    def test_commit_update(self):
        data = {"sha": "02c98f480c57c02d1db3d679e8b601695f20a4ef",
                "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org"}
        Commit.objects.create(**data)
        response = self.c.patch('/api/commits/%s' % data['sha'],
                json.dumps({'seen': True}))
        self.assertEqual(response.status_code, 200)
        commit = Commit.objects.filter(sha=data['sha']).first()
        self.assertTrue(commit.seen)

    def test_commit_filter(self):
        data = [{"sha": "1824bbbff1341e253a891a804651b6338f8008e4",
            "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org",},
            {"sha": "02c98f480c57c02d1db3d679e8b601695f20a4ef",
                "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org"},
            {"sha": "4e05952a8a75af6df625415db612d3a9a1322682",
                "name": "Brian White", "email": "mscdex@mscdex.net",},
            {"sha": "22d7dc221211678dd1d5ce30d298791df7dfd956",
                "name": "Rich Trott", "email": "rtrott@gmail.com",},
            {"sha": "172be50fe173ee24cdfec8b5cb2b54b28f74557a",
                "name": "Roman Reiss", "email": "me@silverwind.io",},
            {"sha": "4c05d6a0b7db5bde1900843286996cc22edc6fac",
                "name": "Rich Trott", "email": "rtrott@gmail.com",},
            {"sha": "0d4bbf757c097477fd94d560765b1025fb3d7e7e",
                "name": "Rich Trott", "email": "rtrott@gmail.com",}]
        for d in data:
            Commit.objects.create(**d)

        response = self.c.get('/api/commits')
        self.assertEqual(response.status_code, 200)
        self.assertIn('commits', response.json())
        self.assertEqual(len(response.json()['commits']), len(data))

        response = self.c.get('/api/commits', {'email': 'rtrott@gmail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('commits', response.json())
        self.assertEqual(len(response.json()['commits']), 3)

        response = self.c.get('/api/commits', {'name': 'Shigeki Ohtsu'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('commits', response.json())
        self.assertEqual(len(response.json()['commits']), 2)

        response = self.c.get('/api/commits', {'name': 'John Doe'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('commits', response.json())
        self.assertEqual(len(response.json()['commits']), 0)

    def test_commit_get(self):
        data = {"sha": "02c98f480c57c02d1db3d679e8b601695f20a4ef",
                "name": "Shigeki Ohtsu", "email": "ohtsu@ohtsu.org"}
        Commit.objects.create(**data)
        response = self.c.get('/api/commits/%s' % data['sha'])
        self.assertEqual(response.status_code, 200)
        self.assertIn('name', response.json())
        self.assertEqual(response.json()['name'], data['name'])

        response = self.c.get('/api/commits/bb5c84a1a7e29f6e5bca619dc73c78348326c1b7')
        self.assertEqual(response.status_code, 404)
