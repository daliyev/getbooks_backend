from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from library.serializers import BookViewHistorySerializer
from drf_yasg.utils import swagger_auto_schema


class BookViewHistoryCreate(APIView):
    serializer_class = BookViewHistorySerializer

    @swagger_auto_schema(request_body=BookViewHistorySerializer)
    def post(self, request):
        serializer = BookViewHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
