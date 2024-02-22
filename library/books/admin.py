from django.contrib import admin

from . import models


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'price')
    ordering = ('-id',)
    readonly_fields = ('created_at',)
    list_filter = ('authors',)


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['name', 'pseudonym']
    list_display = ('name', 'id', 'pseudonym')
    ordering = ('-id',)


class PublisherAdmin(admin.ModelAdmin):
    search_fields = ['name']


class AuthorDetailsAdmin(admin.ModelAdmin):
    search_fields = ['author']


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.AuthorDetails, AuthorDetailsAdmin)
