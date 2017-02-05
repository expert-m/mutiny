from rest_framework import generics
from rest_framework import permissions

from project.apps.projects.serializers import ProjectSerializer
from project.utils import StandardResultsSetPagination
from .models import *


class ApiProjectListView(generics.ListAPIView):
    model = Project
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultsSetPagination
    queryset = Project.objects.filter(is_published=True, is_closed=False).order_by('-created')


class ApiProjectDetailView(generics.RetrieveAPIView):
    model = Project
    serializer_class = ProjectSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Project.objects.filter(is_published=True, is_closed=False)

