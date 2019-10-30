from django.db import models

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=100)
    body = models.TextField()
