from django.shortcuts import render


urlpatterns = [
    url(r'^api/auth/', ApiAuthView.as_view()),
    url(r'^api/profile/', ApiProfileView.as_view()),
]
