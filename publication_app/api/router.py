from rest_framework import routers

from .views.publications import PostsViewSet


api_router = routers.DefaultRouter()

api_router.register('post', PostsViewSet)
