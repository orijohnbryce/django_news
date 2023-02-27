from django.db import models

# Create your models here.


class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title