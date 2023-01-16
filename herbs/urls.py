from django.urls import path, include
from views import (
    CountryListView,
    CategoryListView,
    FlavorListView,
    HerbListView,
    HerbDetailsView
)

urlpatterns = [
    path('', views.starting_page, name="starting-page"),
    path('herbs', HerbListView.as_view(), name="herb-list"),
    path('herbs/<slug:slug>', HerbDetailsView, name="herb-detail-page")
]