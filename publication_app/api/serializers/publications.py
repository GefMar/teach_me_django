from rest_framework import serializers

from media_app.api.serializers.media import MediaSerializer
from tags_app.api.serializers.tag import TagSerializer
from ...models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ['id', "user", ]
        exclude = ['is_public', ]
        extra_kwargs = {
            'file': {"required": True, 'write_only': True, "help_text": "ID Медиа Файла", }
        }

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source="user"
    )
    media = MediaSerializer(source='file', allow_null=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    # user_name = serializers.CharField(source='user.username', read_only=True, allow_null=False)

    def get_likes_count(self, instance) -> int:
        return instance.likes.count()

    def get_comments_count(self, instance) -> int:
        return instance.comments.count()

# TODO: API интерфейс получить все Посты
# TODO: API интерфейс Получить все Теги
# TODO: *** Получить посты определенного тега
