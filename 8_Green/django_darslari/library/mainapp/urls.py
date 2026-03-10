from django.urls import path, include
from rest_framework import routers
from .views import Category_ViewSet, Author_ViewSet, Book_ViewSet

router = routers.DefaultRouter()
router.register("categorys", Category_ViewSet)
router.register("authors", Author_ViewSet)
router.register("books", Book_ViewSet)

urlpatterns = [
    path("", include(router.urls))
]
