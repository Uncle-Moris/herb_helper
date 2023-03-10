from django.urls import path
from .views import (
    CountryListView,
    CategoryListView,
    FlavorListView,
    HerbListView,
    HerbDetailsView
)
app_name = "herbs"

urlpatterns = [
    path('list', HerbListView.as_view(), name="herb-list"),
    path('<slug:slug>', HerbDetailsView.as_view(), name="herb-detail-page"),
    path('<slug:slug>', FlavorListView.as_view()),
    path('<slug:slug>', CategoryListView.as_view()),
    path('<slug:slug>', CountryListView.as_view())
]
