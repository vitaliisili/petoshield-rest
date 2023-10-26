from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.policy import views

app_name = 'insurance'

router = DefaultRouter()
router.register('service-providers', views.ServiceProviderViewSet, basename='service-providers'),
router.register('policies', views.PolicyViewSet, basename='policies'),
router.register('insurance-cases', views.InsuranceCaseViewSet, basename='insurance-cases'),
router.register('incoming-invoices', views.IncomingInvoiceViewSet, basename='incoming-invoices'),

urlpatterns = [
    path('', include(router.urls))
]