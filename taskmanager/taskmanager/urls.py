from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # This adds login/logout views
    path('', include('tasks.urls')),  # Your app URLs
]
