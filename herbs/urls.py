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
    path('<slug:slug>', HerbDetailsView.as_view(), name="herb-detail-page")
]