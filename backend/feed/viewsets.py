from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from feed.models import Feed
from feed.serializers import FeedSerializer


class FeedViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def get_queryset(self):
        return Feed.objects.filter(user=self.request.user)
