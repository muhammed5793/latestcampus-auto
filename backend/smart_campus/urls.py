from django.contrib import admin
from django.urls import path, include
from accounts.views import CustomTokenView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔐 JWT Authentication
    path('api/auth/token/', CustomTokenView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/dashboard/', include('dashboard.urls')),
]
