from django.contrib import admin

from .models import Band


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


admin.site.register(Band, BandAdmin)
