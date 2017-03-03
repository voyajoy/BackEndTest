from django.db import models

class Commit(models.Model):
    sha = models.CharField(max_length=40, unique=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    seen = models.BooleanField(default=False)

    def to_dict(self):
        return dict(
            sha=self.sha,
            name=self.name,
            email=self.email,
            seen=self.seen)
