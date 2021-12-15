from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.comment import CommentSerializer
from ...models import Comment


class CommentViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
