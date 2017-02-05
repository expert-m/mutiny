from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/posts/$', ApiPostListView.as_view()),
    url(r'^api/posts/(?P<pk>\d+)/$', ApiPostDetailView.as_view()),
]
