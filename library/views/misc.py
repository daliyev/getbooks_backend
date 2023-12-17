from rest_framework import viewsets, generics

# from rest_framework.permissions import IsAuthenticated
from custom_auth.models import CustomUser
from library.models import Review, SubCategory, Category, Author, Book, LikedBook
from library.permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly, IsAuthenticatedOrReadOnly
from library.serializers import ReviewSerializer, SubCategorySerializer, CategorySerializer, LikedBookSerializer
from custom_auth.serializer import CustomUserSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsStaffOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsStaffOrReadOnly]
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsStaffOrReadOnly]
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class LikedBookViewSet(viewsets.ModelViewSet):
    queryset = LikedBook.objects.all()
    serializer_class = LikedBookSerializer