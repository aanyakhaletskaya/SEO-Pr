from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap

from venue import views as venue_views
from venue.sitemaps import StaticViewSitemap, HallSitemap, PosterSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "halls": HallSitemap,
    "posters": PosterSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    path("robots.txt", venue_views.robots_txt, name="robots_txt"),
    path("", include("venue.urls")),
]