from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/auth/$', ApiAuthView.as_view()),
    url(r'^api/profile/$', ApiProfileView.as_view()),
    url(r'^api/users/$', ApiUserListView.as_view()),
    url(r'^api/users/(?P<pk>\d+)/$', ApiUserDetailView.as_view()),
]
