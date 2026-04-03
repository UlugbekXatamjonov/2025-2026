from django.urls import path, include
from rest_framework import routers
from .views import Category_ViewSet, Author_ViewSet, Book_ViewSet, Category_Books_Viewset

router = routers.DefaultRouter()
router.register("category_books", Category_Books_Viewset, basename='category_books')
router.register("categorys", Category_ViewSet, basename="categorys")
router.register("authors", Author_ViewSet)
router.register("books", Book_ViewSet)

urlpatterns = [
    path("", include(router.urls))
]
