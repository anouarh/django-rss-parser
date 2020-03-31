from django.shortcuts import render
from .models import Feed
from .serializers import FeedSerializer

from rest_framework.viewsets import ModelViewSet

class FeedViewSet(ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer
    
