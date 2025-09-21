from django.contrib import admin
from .models import Activity, Progress
from .models import Feedback

admin.site.register(Feedback)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'type', 'level', 'min_age', 'max_age',
        'environment', 'is_active', 'created_at'
    )
    list_filter = (
        'type', 'environment', 'is_active', 'level',
        'min_age', 'max_age'
    )
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'description')
        }),
        ('Skill & Environment', {
            'fields': ('type', 'environment')
        }),
        ('Age & Difficulty', {
            'fields': ('level', 'min_age', 'max_age')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
    )


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'activity', 'completed_on', 'rating')
    list_filter = ('completed_on', 'rating')
    search_fields = ('user__username', 'activity__title')
    ordering = ('-completed_on',)
