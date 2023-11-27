from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'dessert'
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:dessert_id>/", views.dessert_detail, name="dessert_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
