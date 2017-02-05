from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^home/$', IndexView.as_view())
]
