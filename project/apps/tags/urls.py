from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/tags/$', ApiTagListView.as_view()),
]
