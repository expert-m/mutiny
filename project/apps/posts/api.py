from rest_framework import generics
from rest_framework import permissions

from project.apps.posts.serializers import PostSerializer
from project.utils import StandardResultsSetPagination
from .models import *


class ApiPostListView(generics.ListAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultsSetPagination
    queryset = Post.objects.filter(is_published=True).order_by('-created')


class ApiPostDetailView(generics.RetrieveAPIView):
    model = Post
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Post.objects.filter(is_published=True)
