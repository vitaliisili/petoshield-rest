from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.user import views

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
