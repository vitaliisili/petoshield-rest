from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api/auth/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/', include('apps.user.urls')),
    path('api/pet-profile/', include('apps.pet.urls')),
    path('api/insurance/', include('apps.policy.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
