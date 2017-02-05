from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


class ApiSubscriptionView(APIView):
    permission_classes = (permissions.AllowAny,)

    def put(self, request):
        try:
            MailList.objects.create(email=request.POST.get('email'))
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_201_CREATED)

    def delete(self, request):
        try:
            MailList.objects.get(
                email=request.POST.get('email'),
                code=request.POST.get('code')
            ).delete()
        except Exception as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_200_OK)
