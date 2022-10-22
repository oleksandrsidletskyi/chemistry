from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
