from django.contrib import admin

from .models import Badge, Developer, Feature, Genre, Platform, Publisher


class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name", "nationality", "still_active"]
    ordering = ["name"]
    search_fields = ["name"]
    list_filter = ["nationality"]


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ["name", "nationality", "entity", "still_active"]
    ordering = ["name"]
    search_fields = ["name"]
    list_filter = ["nationality"]


class PlatformAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]


class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]


class FeatureAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]


class BadgesAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Platform, PlatformAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Badge, BadgesAdmin)
