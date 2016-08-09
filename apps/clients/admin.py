# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Client, Testimonial


@admin.register(Client)
class Clientdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link')
    search_fields = ('id', 'name', 'link', 'description')
    ordering = ['id', 'name', 'link']
    list_display_links = ('id', 'name', 'link')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('id', 'title')
    ordering = ['id', 'title']
    list_display_links = ('id', 'title')

