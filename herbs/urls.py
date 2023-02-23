from django.urls import path, include
from .views import (
    CountryListView,
    CategoryListView,
    FlavorListView,
    HerbListView,
    HerbDetailsView
)

urlpatterns = [
    # path('', views.starting_page, name="starting-page"),
    path('', HerbListView.as_view(), name="herb-list"),
    path('<slug:slug>', HerbDetailsView.as_view(), name="herb-detail-page"),

    path('<slug:slug>', FlavorListView.as_view()),
    path('<slug:slug>', CategoryListView.as_view()),
    path('<slug:slug>', CountryListView.as_view())
]