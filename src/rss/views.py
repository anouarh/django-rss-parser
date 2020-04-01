import feedparser

from django.http import JsonResponse
from django.shortcuts import render

from .models import Feed
from .serializers import FeedSerializer

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


class FeedViewSet(ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    @action(detail=True, methods=["GET"])
    def items(self, request, pk):
        feed = Feed.objects.get(pk=pk)

        items = []

        rss = feedparser.parse(feed.link)

        items.extend(rss["items"])

        return JsonResponse(items, safe=False)
