from django.contrib import admin

from .models import Rating


class RatingAdmin(admin.ModelAdmin):
    list_display = ["game", "user", "score", "content"]
    search_fields = ["game__title"]
    ordering = ["game__title"]
    list_filter = ["score"]


admin.site.register(Rating, RatingAdmin)
