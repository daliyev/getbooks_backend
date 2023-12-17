from rest_framework import serializers
from library.models import Category, SubCategory, Book, Author, Publisher, Review, LikedBook, BookViewHistory
from custom_auth.models import CustomUser


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'is_active']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class LikedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikedBook
        fields = [
            'user_id',
            'book_copy_id'
        ]


class BookViewHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BookViewHistory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class LikedBookSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="customuser")
    book = serializers.CharField(source="book")

    class Meta:
        model = LikedBook
        fields = [
            "user",
            "book",
        ]
