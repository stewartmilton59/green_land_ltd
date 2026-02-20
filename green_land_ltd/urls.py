from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("arusha_milk_ltd.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.index_title = "Arush_Milk_ltd"
admin.site.site_header = "Arush_Milk_ltd"
admin.site.site_title = "Arush_Milk_ltd"
