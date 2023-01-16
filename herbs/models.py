from django.db import models


class Category(models.Model):
    class Meta:
        ordering = ('pk',)

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Country(models.Model):
    class Meta:
        ordering = ('name',)

    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return f'{self.name}'


class Flavor(models.Model):
    class Meta:
        ordering = ('name',)

    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'


class Herb(models.Model):
    name = models.CharField(unique=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    country_of_origin = models.ManyToManyField(Country)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    