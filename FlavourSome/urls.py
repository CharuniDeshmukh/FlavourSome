
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FlavourApp.urls')),
    path('Flavoursome/', include('FlavourApp.urls')),
    path('Flavoursome/feedback/', include('FlavourApp.urls')),
    path('Flavoursome/register/', include('FlavourApp.urls')),
    path('Flavoursome/login/', include('FlavourApp.urls')),
    path('Flavoursome/cart/', include('FlavourApp.urls')),
    path('Flavoursome/orders/', include('FlavourApp.urls')),
    path('Flavoursome/checkout/', include('FlavourApp.urls')),
    path('Flavoursome/updater/', include('FlavourApp.urls')),
    path('Flavoursome/handler/', include('FlavourApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
