from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()

    published = models.BooleanField(default=False)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
