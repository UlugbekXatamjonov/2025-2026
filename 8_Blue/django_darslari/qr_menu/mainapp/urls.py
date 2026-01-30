from django.urls import path, include
from rest_framework import routers
from .views import Category_List_Viewset, Category_Viewset


router = routers.DefaultRouter()
router.register(r'category-list', Category_List_Viewset, basename='category-list')
router.register(r'category', Category_Viewset, basename='category')


urlpatterns = [
    path('', include(router.urls)),
]

