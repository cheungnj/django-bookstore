from django.contrib import admin

from store.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock')


admin.site.register(Book, BookAdmin)
