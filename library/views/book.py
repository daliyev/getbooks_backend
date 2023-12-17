from django.db import models
from django.db.models import Count
from rest_framework import viewsets, generics
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from library.filters import SubCategoryFilter
from library.models import Book, Author, Category, SubCategory
from library.permissions import IsStaffOrReadOnly
from library.serializers import CategorySerializer, AuthorSerializer, SubCategorySerializer, BookWriteSerializer, BookReadSerializer
# for media
from rest_framework.parsers import FormParser, MultiPartParser
from django.db.models import Count, Avg, Case, When, F
from library.services import *


class CustomPagination(PageNumberPagination):
    page_size = 15


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsStaffOrReadOnly]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class AuthorViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsStaffOrReadOnly]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().annotate()

    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return BookWriteSerializer

        return BookReadSerializer

    # def get_permissions(self):
    #     # if self.action in ("create", "update", "partial_update", "destroy"):
    #     #     # self.permission_classes = [IsStaffOrReadOnly]
    #
    #     return super().get_permissions()


# @api_view(['GET'])
# def home_page(request):
#     books = get_book_list()
#     categories = get_category()
#     subcategories = get_subcategory()
#
#     context = {
#         "books": books,
#         "categories": categories,
#         "subcategories": subcategories
#     }
#
#     return Response(context)
#
#
# @api_view(['GET'])
# def book_list_by_subcategory_id(request, sc_id):
#     return Response(get_book_list_by_subcategory_id(sc_id))
