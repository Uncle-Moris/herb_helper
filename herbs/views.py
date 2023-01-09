from django.shortcuts import render
from django.views.generic import ListView,DeleteView

from .models import Herb, Category, Country, Flavor


class HerbListView(ListView):
    model = Herb

    def get_context_data(self, *, object_list=None, **kwargs):
        pass


class HerbDetailsViev(DeleteView):

    model = Herb
    template_name = 'herbs/'
    def get_queryset(self):
        pass


class CategoryListView(ListView):
    model = Category
    pass


class FlavorListView(ListView):
    model = Flavor
    pass


class CountryListView(ListView):
    model = Country
    pass
