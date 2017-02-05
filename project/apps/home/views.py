from django.shortcuts import render
from django.views.generic import TemplateView
from project.apps.feedback.api import ApiFeedbackCreateView


# def get_client_ip(request):
#     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
#     if x_forwarded_for:
#         ip = x_forwarded_for.split(',')[0]
#     else:
#         ip = request.META.get('REMOTE_ADDR')
#     return ip


class IndexView(TemplateView):
    template_name = 'home.html'

