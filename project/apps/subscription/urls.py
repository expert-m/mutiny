from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/subscription/', ApiSubscriptionView.as_view()),
]
