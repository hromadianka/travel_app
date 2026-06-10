from django.urls import path
from .views import (
    AddPlaceAPIView,
    ListPlacesAPIView,
    RetrievePlaceAPIView,
    UpdatePlaceAPIView
)

urlpatterns = [
    path("projects/<int:project_id>/places/", AddPlaceAPIView.as_view()),
    path("projects/<int:project_id>/places/list/", ListPlacesAPIView.as_view()),
    path("projects/<int:project_id>/places/<int:place_id>/", RetrievePlaceAPIView.as_view()),
    path("projects/<int:project_id>/places/<int:place_id>/update/", UpdatePlaceAPIView.as_view()),
]