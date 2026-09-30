from django.contrib import admin
from django.urls import include, path

from venue import views as venue_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("robots.txt", venue_views.robots_txt, name="robots_txt"),
    path("", include("venue.urls")),
]