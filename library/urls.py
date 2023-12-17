from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import *
from library.services import BookViewHistoryCreate

router = DefaultRouter()
router.register(r'book', BookViewSet)
router.register(r'user', UserViewSet)
router.register(r'author', AuthorViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'subcategory', SubCategoryViewSet)
# router.register(r'liked-book', LikedBookViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('home', home_page, name='list_books_with_authors'),
    # path('subcategory/<int:sc_id>/', book_list_by_subcategory_id, name='book_list_by_subcategory_id'),
    path('book-view/', BookViewHistoryCreate.as_view(), name='book-author-view-history')
]
