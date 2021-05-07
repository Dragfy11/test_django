from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=400)
    body = models.TextField()
    Author = models.CharField(max_length=200)
    date = models.DateField(auto_now=True)