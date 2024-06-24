from django.contrib import admin

from .models import (
    Topic,
    Post,
    Comment,
    Mensaje
)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ["topics"]
    list_display = ["title", "is_public", "created", "updated"]

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    list_display = ["nombre", "email", "visto", "fecha"]


admin.site.register(Topic)
admin.site.register(Comment)

