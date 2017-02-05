from django.conf.urls import url
from .api import *


urlpatterns = [
    url(r'^api/feedback/$', ApiFeedbackCreateView.as_view()),
]
