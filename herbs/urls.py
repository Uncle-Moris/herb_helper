from django.urls import path, include
from views import (
    CountryListView,
    CategoryListView,
    FlavorListView,
    HerbListView
)

urlpatterns = [
    path('', views.starting_page, name="starting-page"),
    path('herbs', HerbListView.as_view(), name="herb-list"),
    path('herbs/<slug:slug>', views.post_detail, name="herb-detail-page")
]