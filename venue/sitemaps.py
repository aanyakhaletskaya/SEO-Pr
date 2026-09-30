from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Hall, Poster


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            "venue:home",
            "venue:hall_list",
            "venue:menu",
            "venue:events",
            "venue:poster_list",
            "venue:contacts",
            "venue:gallery",
        ]

    def location(self, item):
        return reverse(item)


class HallSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Hall.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at


class PosterSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Poster.objects.filter(is_published=True)