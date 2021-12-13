from rest_framework import serializers

from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
        read_only_fields = ['id', "user", "is_public"]

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )

# TODO: API интерфейс получить все Посты
# TODO: API интерфейс Получить все Теги
# TODO: *** Получить посты определенного тега
