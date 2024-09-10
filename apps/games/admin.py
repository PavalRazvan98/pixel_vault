from django.contrib import admin

from .models import Game, SystemRequirement


class GameAdmin(admin.ModelAdmin):
    list_display = ["title", "pegi_rating", "release_date", "display_publishers", "display_developer", "display_genres", "usd_price", ]
    search_fields = ["title"]
    ordering = ["title"]
    list_filter = ["genres"]


    def display_publishers(self, obj):
        # Get all publisher names and join them with a comma
        return ", ".join(publisher.name for publisher in obj.publisher.all())
    display_publishers.short_description = 'Publishers'  # Set the column header in the admin

    def display_developer(self, obj):
        # Get all developer names and join them with a comma
        return ", ".join(developer.name for developer in obj.developer.all())
    display_developer.short_description = 'Developer'  # Set the column header in the admin

    def display_genres(self, obj):
        return ", ".join(genres.name for genres in obj.genres.all())
    display_genres.short_description = 'Genres'


class SystemRequirementAdmin(admin.ModelAdmin):
    list_display = ["game", "type", "os"]
    ordering = ["type"]
    list_filter = ["os"]


admin.site.register(Game, GameAdmin)
admin.site.register(SystemRequirement,SystemRequirementAdmin)
