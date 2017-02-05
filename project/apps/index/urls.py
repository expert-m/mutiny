from django.conf.urls import url
from .views import *


urlpatterns = [
    url(r'^(?!home/|api/)', IndexView.as_view(), name='home'),
]
