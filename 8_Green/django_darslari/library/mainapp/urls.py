from django.urls import path, include
from rest_framework import routers
from .views import Category_ViewSet, Author_ViewSet, Book_ViewSet, Category_Books_Viewset, Author_Book_Viewset

router = routers.DefaultRouter()
router.register(r"category_books", Category_Books_Viewset, basename='category_books')
router.register(r"categorys", Category_ViewSet, basename="categorys")
router.register(r"authors_books", Author_Book_Viewset, basename="authors_books")
router.register(r"authors", Author_ViewSet, basename="authors")
router.register(r"books", Book_ViewSet)

urlpatterns = [
    path("", include(router.urls))
]
