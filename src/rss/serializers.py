from rest_framework import serializers
from .models import Feed


class FeedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"