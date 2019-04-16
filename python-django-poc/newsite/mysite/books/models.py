from django.db import models


class Book(models.Model):

    def __str__(self):
        return self.name + "-" + self.author + "-" + self.price + "-" + self.type

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
