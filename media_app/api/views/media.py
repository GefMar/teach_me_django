from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.viewsets import GenericViewSet

from ..serializers.media import MediaSerializer
from ...models import Media


class MediaViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer
    parser_classes = [MultiPartParser, JSONParser]
