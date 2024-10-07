from django.contrib import admin
from . import models


class BrandsAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'created_at', 'updated_at']
    search_fields = ['name',]


admin.site.register(models.Brand, BrandsAdmin)
