from rest_framework import serializers
from ...models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        exclude = ('user',)

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )
    
