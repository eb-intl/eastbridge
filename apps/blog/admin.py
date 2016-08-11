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
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name', 'description')
    ordering = ['order', 'name', 'description']
    list_display_links = ('id', 'name')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created', 'publish')
    search_fields = ('id', 'title', 'description', 'body')
    ordering = ['id', 'title', 'description']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('tags', 'image', 'files')
