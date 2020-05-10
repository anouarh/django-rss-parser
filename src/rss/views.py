import feedparser

from django.http import JsonResponse
from django.shortcuts import render

from .models import Newspaper
from .serializers import NewspaperSerializer

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


class NewspaperViewSet(ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer

    @action(detail=True, methods=["GET"])
    def articles(self, request, pk):
        feed = Newspaper.objects.get(pk=pk)

        items = []

        rss = feedparser.parse(feed.link)

        items.extend(rss["items"])

        return JsonResponse(items, safe=False)