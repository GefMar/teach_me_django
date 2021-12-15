from rest_framework import routers

from .views.likes import LikeViewSet


api_router = routers.DefaultRouter()

api_router.register('like', LikeViewSet)
