from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.base.urls')), 
    path('groups/', include('apps.rooms.urls'))
]

# This is where we handle 'media' root.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
