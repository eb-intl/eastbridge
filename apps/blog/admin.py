# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Article, Tag, ArticleFile


@admin.register(ArticleFile)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'title')
    search_fields = ('id', 'file', 'title', 'description')
    ordering = ['title']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'visible', 'short_name', 'long_name')
    search_fields = ('id', 'short_name', 'description')
    ordering = ['order', 'short_name', 'description']
    list_display_links = ('id', 'short_name', 'long_name')
    prepopulated_fields = {
        'slug': ('long_name', ), 'long_name': ('short_name', )}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created', 'publish')
    search_fields = ('id', 'title', 'description', 'body')
    ordering = ['id', 'title', 'description']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('tags', 'image', 'files')
