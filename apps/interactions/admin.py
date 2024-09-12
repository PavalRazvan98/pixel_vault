from django.contrib import admin

from .models import Session


class SessionAdmin(admin.ModelAdmin):
    list_display = ["game", "user", "time_play", "last_play", "ip_address"]
    search_fields = ["user__username"]
    ordering = ["game__title"]
    list_filter = ["game__title"]


admin.site.register(Session, SessionAdmin)
