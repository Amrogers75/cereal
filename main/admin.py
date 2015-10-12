from django.contrib import admin
from main.models import Cereal, Manufacturer
# Register your models here.


class CerealAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer')

admin.site.register(Cereal)
admin.site.register(Manufacturer)