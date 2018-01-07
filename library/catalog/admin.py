from django.contrib import admin
from .models import Books, Issues, Students


class Books_Admin(admin.ModelAdmin):
 list_display = ('title', 'author','available')
 list_filter = ('title', 'author','available')
 pass

admin.site.register(Books,Books_Admin)

class Students_Admin(admin.ModelAdmin):
 list_display = ('s_id', 'name', 'class_name','loans')
 list_filter = ('s_id', 'name', 'class_name','loans')
 pass

admin.site.register(Students,Students_Admin)

class Issues_Admin(admin.ModelAdmin):
 list_display = ('name', 'title', 'author','issue','return_d')
 list_filter =('name', 'title', 'author','issue','return_d')
 pass

admin.site.register(Issues,Issues_Admin)
