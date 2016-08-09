# -*- coding: utf-8 -*-
"""
"""
from django.contrib import admin

from models import Office, Employee, Position, Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name', 'slug', 'description')
    ordering = ['id', 'name', 'slug', 'description']
    #list_editable = ('active',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'primary')
    search_fields = ('id', 'name', 'slug', 'address', 'primary')
    ordering = ['id', 'name', 'slug', 'address', 'primary']
    #list_editable = ('active',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'name', 'description', 'featured')
    search_fields = ('id', 'order', 'name', 'description', 'featured')
    ordering = ['id', 'order', 'name', 'description', 'featured']
    #list_editable = ('active',)
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name', 'description')
    ordering = ['id', 'name', 'description']
    #list_editable = ('active',)
    list_display_links = ('id', 'name')

