from django.contrib import admin

from .models import Post


# admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', "create_date", 'title',)
    ordering = ("-create_date", '-id',)
    readonly_fields = ("create_date",)
