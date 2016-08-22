# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Service, ServiceGroup, ProcessItem, Process


@admin.register(ProcessItem)
class ProcessItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title', 'description')
    search_fields = ('id', 'title', 'slug', 'description')
    ordering = ['order', 'id', 'title', 'slug', 'description']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('id', 'title', 'slug', 'description')
    ordering = ['id', 'title', 'slug', 'description']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('items', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title', 'description')
    search_fields = ('id', 'title', 'slug', 'description', 'text')
    ordering = ['order', 'id', 'title', 'slug', 'description']
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ServiceGroup)
class ServiceGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'title')
    search_fields = ('id', 'title')
    ordering = ['order', 'id', 'title']
    list_display_links = ('id', 'title')

