from django.db import models

from django.utils import timezone

class Client(models.Model):
    """You may work with different clients for same/different projects,
    hence let's create a model for client  """
    name = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)

class Project(models.Model):
    name = models.CharField(max_length=200)
    client_id = models.ForeignKey('Client', null=True)

    def __str__(self):
        return '<{}> {}'.format(self.client_id.name, self.name)


# Create your models here.
class Entry(models.Model):
    start = models.DateTimeField(default=timezone.now)
    stop = models.DateTimeField(blank=True, null=True)
    project = models.ForeignKey('Project')
    description = models.CharField(max_length=200)

    def __str__(self):
        return '[{} - {}] ({}) {}'.format(self.start, self.stop, self.project, self.description)

    def is_finished(self):
        return self.stop is not None
