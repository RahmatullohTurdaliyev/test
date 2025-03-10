from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.title
