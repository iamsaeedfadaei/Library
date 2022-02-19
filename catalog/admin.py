from django.contrib import admin
from .models import Book, Author, BookInstance, Genre

#creating inline for copy instances in book model by TabularInline.
# we have foreignkey from bookinstances to book and from book to authors --> just the way of foreignkey!
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

class BooksInline(admin.TabularInline):
    model = Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'display_genre')
    inlines = [BooksInstanceInline]
    #  we cant make foreign key a display link :)
    # list_display_links = ('author')




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    list_display_links = ('first_name', 'last_name')
    # The fields attribute lists just those fields that are to be displayed on the form,
    # in order. Fields are displayed vertically by default,
    # but will display horizontally if you further group them in a tuple(as shown in the "date" fields above).
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]


admin.site.register(Genre)




@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'status')
    list_filter = ('due_back', 'status')

    # adding different sections to bookinstance admin page
    fieldsets = (
        ('Book Information:',{
        'fields': ('book', 'imprint', 'id')
    }),
    ('Book Availability:',{
        'fields': ('status', 'due_back')
    })
    )
