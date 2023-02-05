from django.contrib import admin

from triangle.models import Log, Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'email')
    search_fields = ['first_name', 'last_name']


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('path', 'method', 'timestamp', 'data')
    search_fields = ('path', 'method')
    list_filter = ('method', 'timestamp')
    ordering = ('-timestamp',)
