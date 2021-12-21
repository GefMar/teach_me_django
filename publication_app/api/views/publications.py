from rest_framework import filters
from django.db.models import F, Sum, Q, Count
from rest_framework import permissions
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from ..serializers.publications import PostSerializer
from ...models import Post


class TestPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return True

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False


class PostsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    permission_classes = [TestPermission, ]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter, ]
    ordering_fields = ['create_date', ]

    def list(self, request, *args, **kwargs):
        # Post.objects.annotate(likes_count=Count(F('likes'))).order_by(-F("likes_count"))
        print(1)
