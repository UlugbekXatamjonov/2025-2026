from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .views import CategoryViewSet, CakeViewSet, NewViewSet, Last_cakes_ViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'cake', CakeViewSet)
router.register(r'new', NewViewSet)
router.register(r'last_cakes', Last_cakes_ViewSet, basename='last_cakes')



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
