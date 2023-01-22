from django.shortcuts import render
from django.views.generic import ListView,DeleteView

from .models.models import Herb, Category, Country, Flavor


class HerbListView(ListView):
    model = Herb
    context_object_name = 'herbs_list'


class HerbDetailsView(DeleteView):
    model = Herb
    template_name = "herbs/herb_delete.html"




class CategoryListView(ListView):
    model = Category
    pass


class FlavorListView(ListView):
    model = Flavor
    pass


class CountryListView(ListView):
    model = Country
    pass
