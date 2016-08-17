# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Slide, Layer


@admin.register(Slide)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')
    ordering = ['id', 'title']
    list_display_links = ('id', 'title')


@admin.register(Layer)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id', 'body')
    search_fields = ('id', 'body')
    ordering = ['id', 'body']
    list_display_links = ('id', 'body')

