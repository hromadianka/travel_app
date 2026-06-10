from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import ValidationError
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()

        if project.place_set.filter(visited=True).exists():
            raise ValidationError(
                "Cannot delete project with visited places"
            )

        return super().destroy(request, *args, **kwargs)