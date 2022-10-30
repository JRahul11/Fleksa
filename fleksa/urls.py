from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentication Routing
    path('auth/', include('auth_app.urls')),
    
    # Menu Routing
    path('', include('menu_app.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)