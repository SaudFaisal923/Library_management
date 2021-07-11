from django.contrib import admin
from .models import Books,IssueBook
from django.contrib.auth.models import User
# Register your models here.
class BooksAdmin(admin.ModelAdmin):
    list_display=['book_name','author','publication','price','rating','available']
class IssueBookAdmin(admin.ModelAdmin):

    list_display=['user','book','issue_date','return_date','returned','RetDate','fined']

    # def Book_Names(self,obj):
    #     return "\n".join([p.book_name for p in obj.book.all()])

admin.site.register(Books,BooksAdmin)
admin.site.register(IssueBook,IssueBookAdmin)
