from django.db import models
from projects.models import Project


class Place(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='places',
        on_delete=models.CASCADE
    )

    external_id = models.IntegerField()

    title = models.CharField(max_length=255, blank=True, null=True)

    notes = models.TextField(blank=True, null=True)
    visited = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('project', 'external_id')