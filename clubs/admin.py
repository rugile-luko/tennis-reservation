from django.contrib import admin
from . import models


class CourtAdmin(admin.ModelAdmin):
    list_filter = ['club']


admin.site.register(models.Club)
admin.site.register(models.Court, CourtAdmin)
admin.site.register(models.Reservation)
