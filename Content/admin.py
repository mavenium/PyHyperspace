from django.contrib import admin

from Content import models


class BlogAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'publish',
        'create_time',
        'last_update_time'
    ]
    list_editable = (
        'publish',
    )
    list_filter = (
        'publish',
        'create_time',
        'last_update_time'
    )
    search_fields = (
        'title',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Skill)
