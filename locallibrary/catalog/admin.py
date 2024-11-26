from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)

# Define the admin class
# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
    list_display = ('title', 'author', 'display_genre')


# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    pass
    list_filter = ('status', 'due_back')




