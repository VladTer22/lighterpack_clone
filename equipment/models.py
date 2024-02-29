from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    weight = models.FloatField()
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ItemList(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(Item, related_name='lists')
    owner = models.ForeignKey(User, related_name='lists', on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_lists', blank=True)

    def __str__(self):
        return self.name

