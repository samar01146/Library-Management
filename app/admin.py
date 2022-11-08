from django.contrib import admin
from .models import *

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>USER REGISTRATIONS<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display =('id' , 'email', 'username', 'type')

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>BOOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@admin.register(Book)
class AdminBookAdd(admin.ModelAdmin):
    list_display = ('id','book_id', 'book_name', 'book_price', 'book_author', 'book_dateofpublication', 'book_in_language', )

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>LEND BOOK<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@admin.register(LendBook)
class IssuedBook(admin.ModelAdmin):
    list_display = ('user', 'book', 'issued_date', 'fine', 'tc' )