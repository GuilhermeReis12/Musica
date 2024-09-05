from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'generos', views.GeneroViewSet)
router.register(r'musicas', views.MusicaViewSet)
router.register(r'pastas', views.PastaMusicaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
