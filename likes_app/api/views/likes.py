from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.likes import LikeSerializer
from ...models import Like


class LikeViewSet(GenericViewSet, CreateModelMixin):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
