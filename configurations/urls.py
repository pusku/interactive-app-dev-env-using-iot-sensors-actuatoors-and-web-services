from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from configurations import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('app_dir.main.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()
