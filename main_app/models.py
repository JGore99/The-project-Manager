from django.db import models

class Project(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=300)

def __str__(self):
    return self.name