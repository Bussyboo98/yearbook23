from django.contrib import admin

from django.contrib import admin, messages

from django.http.request import HttpRequest

from year_book.models import *

admin.site.site_header = 'Trailblazers'

# Register your models here.
@admin.register(Blog)
class Blogadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('blog_title',)}
    # search_fields = ['blog_title','post_writer','category','blog_image']
    
    list_display = ['blog_title','post_writer','time_uploaded']
    
@admin.register(Contact_Us)
class ContactAdmin(admin.ModelAdmin):
    list_display=['email','name','subject','message']
    
    def has_add_permission(self, request):
        return False

admin.site.register(Comment)

from .models import Year_Book

class YearBookAdmin(admin.ModelAdmin):
    list_display = ('student_first_name', 'student_last_name', 'email', 'phone_number', 'date_of_birth', 'approve')

admin.site.register(Year_Book, YearBookAdmin)
