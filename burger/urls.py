from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'burger'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:burger_id>/", views.pate_detail, name="burger_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
