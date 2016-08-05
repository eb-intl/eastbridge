# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import TextBox, ContentBox


@admin.register(TextBox)
class TextBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title', 'body')
    search_fields = ('id', 'order', 'title', 'body')
    ordering = ['id', 'order', 'title', 'body']
    list_display_links = ('id', 'title')


@admin.register(ContentBox)
class ContentBoxAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title', 'description')
    search_fields = ('id', 'order', 'title', 'description')
    ordering = ['id', 'order', 'title', 'description']
    list_display_links = ('id', 'title')

