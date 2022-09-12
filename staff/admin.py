from django.contrib import admin

from staff.models import Department, Post, PostType, Staff


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'numbers')


@admin.register(PostType)
class PostTypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'priority')


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('photo', 'fullname', 'department', 'post', 'number', 'published')
    list_display_links = ('photo', 'fullname')
    list_filter = ('department', 'post')
    search_fields = ('_fullname',)
