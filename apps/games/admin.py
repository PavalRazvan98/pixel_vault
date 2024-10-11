from django.contrib import admin

from .models import Game, Media, SystemRequirement


class GameAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "pegi_rating",
        "release_date",
        "display_publishers",
        "display_developers",
        "display_genres",
        "usd_price",
    ]
    search_fields = ["title"]
    ordering = ["title"]
    list_filter = ["genres"]

    def display_publishers(self, obj):
        return ", ".join(publishers.name for publishers in obj.publishers.all())

    display_publishers.short_description = "Publishers"  # Set the column header in the admin

    def display_developers(self, obj):
        return ", ".join(developers.name for developers in obj.developers.all())

    display_developers.short_description = "Developers"  # Set the column header in the admin

    def display_genres(self, obj):
        return ", ".join(genres.name for genres in obj.genres.all())

    display_genres.short_description = "Genres"


class SystemRequirementAdmin(admin.ModelAdmin):
    list_display = ["game", "type", "os"]
    ordering = ["type"]
    list_filter = ["os"]


class MediaAdmin(admin.ModelAdmin):
    list_display = ["game"]


admin.site.register(Game, GameAdmin)
admin.site.register(SystemRequirement, SystemRequirementAdmin)
admin.site.register(Media, MediaAdmin)
