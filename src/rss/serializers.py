from rest_framework import serializers
from .models import Newspaper


class NewspaperSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Newspaper
        fields = "__all__"