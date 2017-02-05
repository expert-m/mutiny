from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/projects/$', ApiProjectListView.as_view()),
    url(r'^api/projects/(?P<pk>\d+)/$', ApiProjectDetailView.as_view()),
]
