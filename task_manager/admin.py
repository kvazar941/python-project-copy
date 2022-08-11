from django.contrib import admin

from .models import my_class


@admin.register(my_class)
class my_classAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
