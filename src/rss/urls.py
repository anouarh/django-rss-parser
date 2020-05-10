from django.urls import include, path
from rest_framework import routers
from rss import views

router = routers.DefaultRouter()
router.register(r'newspapers', views.NewspaperViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
