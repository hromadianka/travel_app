from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from projects.models import Project
from .models import Place
from .serializers import PlaceSerializer
from .services import fetch_artwork


class AddPlaceAPIView(APIView):

    def post(self, request, project_id):
        project = Project.objects.get(id=project_id)

        external_id = request.data.get("external_id")

        if project.places.count() >= 10:
            return Response({"error": "max 10 places"}, status=400)

        if project.places.filter(external_id=external_id).exists():
            return Response({"error": "duplicate"}, status=400)

        data = fetch_artwork(external_id)
        if not data:
            return Response({"error": "invalid external_id"}, status=400)

        place = Place.objects.create(
            project=project,
            external_id=external_id,
            title=data.get("title")
        )

        return Response(PlaceSerializer(place).data, status=201)

class UpdatePlaceAPIView(APIView):

    def patch(self, request, project_id, place_id):
        place = Place.objects.get(id=place_id, project_id=project_id)

        if "notes" in request.data:
            place.notes = request.data["notes"]

        if "visited" in request.data:
            place.visited = request.data["visited"]

        place.save()

        return Response(PlaceSerializer(place).data)

class RetrievePlaceAPIView(APIView):

    def get(self, request, project_id, place_id):
        place = Place.objects.get(id=place_id, project_id=project_id)
        return Response(PlaceSerializer(place).data)

class ListPlacesAPIView(APIView):

    def get(self, request, project_id):
        places = Place.objects.filter(project_id=project_id)
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)