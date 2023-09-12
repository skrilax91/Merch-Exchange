from django.contrib import admin

from .models import Band, Article


class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'year_formed', 'genre')


admin.site.register(Band, BandAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'band')


admin.site.register(Article, ArticleAdmin)
