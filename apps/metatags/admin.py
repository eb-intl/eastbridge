# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'visible', 'short_name', 'long_name')
    search_fields = ('id', 'short_name', 'description')
    ordering = ['order', 'short_name', 'description']
    list_display_links = ('id', 'short_name', 'long_name')
    prepopulated_fields = {
        'slug': ('long_name', ), 'long_name': ('short_name', )}
