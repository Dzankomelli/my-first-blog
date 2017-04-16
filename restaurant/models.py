from django.db import models

class Food(models.Model):
    name = models.CharField('Food name', max_length=100)
    description = models.CharField('Description', max_length=300)
    price = models.IntegerField('Price')
    type = models.ForeignKey('FoodCategory')

    def __str__(self):
        return self.name

class Wine(models.Model):
    name = models.CharField('Wine name', max_length=100)
    price = models.IntegerField('Price')
    type = models.ForeignKey('WineCategory')

    def __str__(self):
        return self.name


class WineCategory(models.Model):
    name = models.CharField('namewine', max_length=100)

    def __str__(self):
        return self.name


class FoodCategory(models.Model):
    name = models.CharField('namefood', max_length=100)

    def __str__(self):
        return self.name
