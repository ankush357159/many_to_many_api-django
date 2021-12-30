from django.contrib import admin

from authors.models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'publisher', 'release_date']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'biography', 'date_of_birth']