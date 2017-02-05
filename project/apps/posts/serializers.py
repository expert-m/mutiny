from rest_framework import serializers
from taggit_serializer.serializers import TagListSerializerField

from project.apps.users.serializers import ShortUserSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()
    # author = ShortUserSerializer()

    class Meta:
        model = Post
        fields = ('id', 'title', 'created', 'content', 'tags', 'author',)
