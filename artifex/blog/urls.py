from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="blog-home")
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)