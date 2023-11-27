from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'pate'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pate_id>/", views.pate_detail, name="pate_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
