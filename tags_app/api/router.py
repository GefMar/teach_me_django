from rest_framework import routers

from .views.tag import TagViewSet


api_router = routers.DefaultRouter()

api_router.register('tag', TagViewSet)
