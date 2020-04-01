from django.urls import include, path
from rest_framework import routers
from rss import views

router = routers.DefaultRouter()
router.register(r'feeds', views.FeedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
