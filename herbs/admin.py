from django.contrib import admin
from . import models





class HerbAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(models.Herb, HerbAdmin)



admin.site.register(models.Category)
admin.site.register(models.Country)
admin.site.register(models.Flavor)