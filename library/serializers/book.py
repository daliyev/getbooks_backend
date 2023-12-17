from django.db.models import Count, Avg
from rest_framework import serializers
from library.models import Book, Author, Review, Category, Publisher, SubCategory, BookActions


class BookActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookActions
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class ReviewSerializer(serializers.Serializer):
    # Only include relevant fields if needed (e.g., rating)
    rating = serializers.IntegerField()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Category
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"


class BookReadSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source="author.get_full_name", read_only=True)
    subcategory = serializers.CharField(source="subcategory.name", read_only=True)
    publisher = serializers.CharField(source="publisher.name", read_only=True)

    class Meta:
        model = Book
        fields = "__all__"

    count_review = serializers.IntegerField(read_only=True)
    average_rating = serializers.FloatField(read_only=True)


class BookWriteSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    subcategory = SubCategorySerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = (
            "author",
            "subcategory",
            "name",
            "about_book",
            "pdf_file",
            "audio_file",
            "image",
            "published_year",
            "publisher"
        )

    def create(self, validated_data):
        subcategory = validated_data.pop("subcategory")
        instance, created = SubCategory.objects.get_or_create(**subcategory)
        book = Book.objects.create(**validated_data, category=instance)

        return book

    def update(self, instance, validated_data):
        if "category" in validated_data:
            nested_serializer = self.fields["subcategory"]
            nested_instance = instance.subcategory
            nested_data = validated_data.pop("subcategory")
            nested_serializer.update(nested_instance, nested_data)

        return super(BookWriteSerializer, self).update(instance, validated_data)
