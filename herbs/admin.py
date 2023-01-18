from django.contrib import admin
from . import models

admin.site.register(models.Herb)
admin.site.register(models.Category)
admin.site.register(models.Country)
admin.site.register(models.Flavor)