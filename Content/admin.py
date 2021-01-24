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


class ContactUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    list_display = [
        'name',
        'email',
        'message',
        'create_time'
    ]
    list_filter = (
        'create_time',
    )
    search_fields = (
        'name',
        'email',
        'message',
    )


admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Skill)
admin.site.register(models.ContactUs, ContactUsAdmin)
