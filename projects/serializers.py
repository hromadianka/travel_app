from rest_framework import serializers
from .models import Project
from places.models import Place
from places.services import fetch_artwork


class ProjectSerializer(serializers.ModelSerializer):
    places = serializers.ListField(
        write_only=True,
        required=False
    )

    class Meta:
        model = Project
        fields = ["id", "name", "description", "start_date", "places"]

    def create(self, validated_data):
        places_data = validated_data.pop('places', [])

        project = Project.objects.create(**validated_data)

        if len(places_data) > 10:
            raise serializers.ValidationError('Max 10 places')

        for ext_id in places_data:
            data = fetch_artwork(ext_id)

            if not data:
                continue  # или raise error

            Place.objects.create(
                project=project,
                external_id=ext_id,
                title=data.get('title')
            )

        return project