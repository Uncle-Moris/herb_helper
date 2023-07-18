from django.contrib import admin
from .models import models


class BaseAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    readonly_fields = ('slug', )
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Category)
admin.site.register(models.Country)
admin.site.register(models.Flavor)


@admin.register(models.Herb)
class HerbAdmin(admin.ModelAdmin):

    readonly_fields = ('slug', )
