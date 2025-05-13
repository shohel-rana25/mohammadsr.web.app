# portfolio/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ContactViewSet

router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path('', include(router.urls)),
    path('api/', include(router.urls)),
]
