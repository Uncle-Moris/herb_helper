from django.db import models
from .abstract_models import BaseModel


class Category(BaseModel):
    class Meta:
        ordering = ('pk',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.name}'


class Country(BaseModel):
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Countries"

    def __str__(self):
        return f'{self.name}'


class Flavor(BaseModel):
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'


class Herb(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    country_of_origin = models.ForeignKey(Country, null=True, blank=True, on_delete=models.PROTECT)
    flavor = models.ManyToManyField(Flavor,null=True, blank=True )
    img = models.ImageField(upload_to='uploads/', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
