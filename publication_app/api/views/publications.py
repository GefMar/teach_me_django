from rest_framework import filters
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.publications import PostSerializer
from ...models import Post


class PostsView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter, ]
    ordering_fields = ['create_date', ]
