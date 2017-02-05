from rest_framework import generics
from rest_framework import permissions

from project.utils import StandardResultsSetPagination
from .models import *
from .serializers import *


class ApiMeetingListView(generics.ListAPIView):
    model = Meeting
    serializer_class = MeetingSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultsSetPagination
    queryset = Meeting.objects.filter(is_published=True, is_closed=False).order_by('-created')


class ApiMeetingDetailView(generics.RetrieveAPIView):
    model = Meeting
    serializer_class = MeetingSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Meeting.objects.filter(is_published=True, is_closed=False)
