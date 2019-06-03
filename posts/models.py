# posts/models.py
from __future__ import unicode_literals
from django.db import models


class Post(models.Model):
    title = models.TextField()
    cover = models.FileField(upload_to='files/')

    def __str__(self):
        return self.title


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)