from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.apps.posts.models import Post


class ApiTagListView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        if request.GET.get('count') and request.GET.get('page'):
            count = int(request.GET.get('count', 0))
            page = int(request.GET.get('page', 1)) - 1

            tags = Post.tags.most_common()[page * count:page * count + count]
            return Response({
                'results': [{'name': tag.name} for tag in tags]
            })
        return Response(status=status.HTTP_400_BAD_REQUEST)
