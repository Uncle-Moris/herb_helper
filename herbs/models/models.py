from django.db import models
from .abstract_models import BaseModel


class Category(BaseModel):
    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return f'{self.name}'


class Country(BaseModel):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class Flavor(BaseModel):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class Herb(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    country_of_origin = models.ManyToManyField(Country)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f'{self.name}'
