from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('checkout/', include('checkout.urls')),
    path('shop/', include('sculptures.urls')),
    path('sculptures/', include('sculptures.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('users.urls')),
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'RossAnthonyDesigns.views.handler404'
handler500 = 'RossAnthonyDesigns.views.handler500'
