from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.tickets import views

router = DefaultRouter()
router.register('tickets', views.TicketViewSet, basename='ticket')
router.register('job-tickets', views.JobTicketViewSet, basename='job-ticket')
router.register('partner-tickets', views.PartnerTicketViewSet, basename='partner-ticket')

urlpatterns = [
    path('', include(router.urls)),
]
