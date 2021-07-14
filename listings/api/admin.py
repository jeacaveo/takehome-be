from django.contrib import admin
from api.models import House


class HouseAdmin(admin.ModelAdmin):
    pass


admin.site.register(House, HouseAdmin)
