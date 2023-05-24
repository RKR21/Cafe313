from django.db import models


class DailySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    date = models.DateTimeField()
    price = models.FloatField()

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name
