from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('project.apps.index.urls')),
    url(r'', include('project.apps.users.urls')),
    url(r'', include('project.apps.home.urls')),
    url(r'', include('project.apps.posts.urls')),
    url(r'', include('project.apps.subscription.urls')),
    url(r'', include('project.apps.tags.urls')),
    url(r'', include('project.apps.projects.urls')),
    url(r'', include('project.apps.meetings.urls')),
]
