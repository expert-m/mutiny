from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class AppRequest:
    @staticmethod
    def search_objects(
            target, data, max_len=100,
            default_sort='id', query_filter=None,
            serializer=None, response=False):

        def app_return(return_data):
            if return_data is None:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            if serializer:
                if type(return_data) is list:
                    for i in range(len(return_data)):
                        return_data[i] = serializer(return_data[i]).data
                else:
                    return_data = serializer(return_data).data
            if not response:
                return return_data
            return Response(return_data)

        sort = data.get('sort', default_sort)
        query_filter = query_filter or {}

        if data.get('id'):
            result = target.objects.get(id=int(data.get('id')))
            return app_return(result)
        elif data.get('count') and data.get('offset'):
            count = int(data.get('count', 0))
            offset = int(data.get('offset', 0))

            count = count if count >= 0 else 0
            offset = offset if offset >= 0 else 0
            count = count if int(data.get('count', 0)) <= max_len else max_len

            result = list(target.objects.filter(**query_filter).order_by(sort)[offset:offset + count])
            return app_return(result)

        return app_return(None)


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'count'
    max_page_size = 100
