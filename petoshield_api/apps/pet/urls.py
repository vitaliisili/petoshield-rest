from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.pet.views import PetViewSet, BreedViewSet

router = DefaultRouter()
router.register('pets', PetViewSet, basename='pets')
router.register('breeds', BreedViewSet, basename='breeds')

urlpatterns = [
    path('', include(router.urls))
]
