import time
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.translation import ugettext_lazy as _

from project.apps.users.serializers import ShortUserSerializer
from project.utils import AppRequest, StandardResultsSetPagination
from .models import *


class ApiAuthView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        user = authenticate(username=request.GET.get('username'), password=request.GET.get('password'))
        if user is None:
            return Response(
                {'detail': _('Неверный логин или пароль.')},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not request.GET.get('remember_me'):
            request.session.set_expiry(0)

        login(request, user)
        return Response(user.profile.serialized())

    # def post(self, request):
    #     request.data['password1'] = request.data['password']
    #     request.data['password2'] = request.data['password']
    #     request.data['g-recaptcha-response'] = request.data['captcha']
    #
    #     form = RegistrationForm(request.data)
    #     if form.is_valid():
    #         user = User.objects.create_user(
    #             username=form.cleaned_data['username'],
    #             password=form.cleaned_data['password1'],
    #             email=form.cleaned_data['email']
    #         )
    #
    #         # profile = Profile.objects.create(user=user)
    #
    #         login(request, user)
    #
    #         return Response(get_user_info(user, profile), status=status.HTTP_201_CREATED)
    #
    #     return Response({'detail': form.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        logout(request)
        return Response()


class ApiProfileView(APIView):
    def get(self, request):
        if request.user.is_authenticated():
            return Response(request.user.profile.serialized())
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ApiUserListView(generics.ListAPIView):
    model = User
    serializer_class = ShortUserSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = StandardResultsSetPagination
    queryset = User.objects.filter(is_active=True)


class ApiUserDetailView(generics.RetrieveAPIView):
    model = User
    serializer_class = ShortUserSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.filter(is_active=True)
