from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',include('watch.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('delete_things/',include('delete_things.urls')),
   ]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)