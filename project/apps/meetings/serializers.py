from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField

from .models import Meeting


class MeetingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meeting
        fields = (
            'id', 'title', 'created',
            'description', 'modified',
            'author',  'start_time',
            'end_time'
        )
