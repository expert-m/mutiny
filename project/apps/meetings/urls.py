from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/meetings/$', ApiMeetingListView.as_view()),
    url(r'^api/meetings/(?P<pk>\d+)/$', ApiMeetingDetailView.as_view()),
]
