from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.payment import views

app_name = 'stripe'

router = DefaultRouter()
router.register('', views.StripeViewSet, basename='payment'),

urlpatterns = [
    path('', include(router.urls))
]
