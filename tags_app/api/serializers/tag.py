from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from ...models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ['posts', ]

    posts_count = serializers.SerializerMethodField()

    # @extend_schema_field(int)
    def get_posts_count(self, instance) -> int:
        return instance.posts.count()


class TagDetailSerializer(TagSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
