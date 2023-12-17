from django.contrib import admin
from library.models import BookActions, Category, SubCategory, Book, Author, Publisher, Review, Notification, LikedBook


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Review)
admin.site.register(Notification)
admin.site.register(LikedBook)
admin.site.register(BookActions)
