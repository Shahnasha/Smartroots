from django.contrib import admin
from .models import Activity, Feedback, Progress

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
    list_display = ('user', 'activity', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('user__username', 'activity__title')
    ordering = ('-timestamp',)
