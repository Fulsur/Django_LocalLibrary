# 网站管理设置
from django.contrib import admin
from .models import Book, Author, BookInstance, Genre

# Register your models here.
#admin.site.register(Book)
@admin.register(Book)       # 加装饰器
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
admin.site.register(Author, AuthorAdmin)        # 不加装饰器


#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status','due_back', 'borrower')
        }),
    )

admin.site.register(Genre)