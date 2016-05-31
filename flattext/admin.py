# coding: utf-8
from django.contrib import admin
from flattext.models import FlatText

@admin.register(FlatText)
class FlatTextAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('slug', 'text_type', 'text', 'processed_text')}),
        ('Note', {'fields': ('note', 'related_url')}),
        )
    list_display = ('slug', 'text_type', 'note', 'related_url')
    list_filter = ('text_type', 'related_url')
    search_fields = ('slug', 'text', 'note')
    readonly_fields = ('processed_text',)
    
