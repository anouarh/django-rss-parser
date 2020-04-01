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
    
    @action(detail=False, methods=["GET"])
    def items(self, request):
        feeds = Feed.objects.all()
        
        items = []
        
        for feed in feeds:
            rss = feedparser.parse(feed.link)
            
            try:
                items.extend(rss["items"])
            except KeyError:
                continue
        
        items = list(reversed(sorted(items, key=lambda item: item["published_parsed"])))
        
        return JsonResponse(items, safe=False)
        
    
    
