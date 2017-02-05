from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField

from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    tech_stack = TagListSerializerField()

    class Meta:
        model = Project
        fields = (
            'id', 'title', 'created',
            'modified', 'tech_stack', 'author',
        )
