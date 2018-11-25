# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from network.models import Area, System


class AreaAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'address'
    )
    readonly_fields = []
    search_fields = ['address']
    ordering = ('address',)


class SystemAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name'
    )
    readonly_fields = []
    search_fields = ['name', 'areas__address',]
    ordering = ('name',)


admin.site.register(Area, AreaAdmin)
admin.site.register(System, SystemAdmin)
