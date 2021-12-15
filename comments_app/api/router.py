from rest_framework import routers

from .views.comment import CommentViewSet


api_router = routers.DefaultRouter()

api_router.register('comment', CommentViewSet)
