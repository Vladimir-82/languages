"""urls language identifier."""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
] + (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
