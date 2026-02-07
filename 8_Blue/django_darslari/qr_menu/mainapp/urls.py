from django.urls import path, include
from rest_framework import routers
from .views import Category_List_Viewset, Category_Viewset, Meal_detail_Viewset


router = routers.DefaultRouter()
router.register(r'category-list', Category_List_Viewset, basename='category-list')
router.register(r'category', Category_Viewset, basename='category')
router.register(r'meal', Meal_detail_Viewset, basename='meal')

urlpatterns = [
    path('', include(router.urls)),
]

