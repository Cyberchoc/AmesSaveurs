from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'salade'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:salade_id>/", views.salade_detail, name="salade_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
