from newspaper import Article
import feedparser

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.shortcuts import render

from .models import Newspaper
from .serializers import NewspaperSerializer

from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet


class NewspaperViewSet(ModelViewSet):
    queryset = Newspaper.objects.all()
    serializer_class = NewspaperSerializer

    @method_decorator(cache_page(60*60))
    @action(detail=True, methods=["GET"])
    def items(self, request, pk):
        feed = Newspaper.objects.get(pk=pk)
        items = []
        url = feed.link
        feed_title = feed.title

        d = feedparser.parse(url)
        
        for entry in d.entries:
            article = Article(entry.link)
            article.download()
            article.parse()
            item = {
                "feed_title": feed_title,
                "title": entry.title,
                "link":  entry.link,
                "published": entry.published,
                "image": article.top_image,
                "text": article.text
            }
            items.append(item)
        

        return JsonResponse(items, safe=False)
