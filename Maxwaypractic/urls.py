
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('panel/admin/access/', admin.site.urls),
    path('', include('food.urls')),
    path('dashboard/panel/access/', include('adminapp.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
