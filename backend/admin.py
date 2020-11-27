from django.contrib import admin
from django.db import models
from backend.models import List, Person, System


class ListAdmin(admin.ModelAdmin):
    model = List


class PersonAdmin(admin.ModelAdmin):
    model = Person


class SystemAdmin(admin.ModelAdmin):
    model = System


admin.site.register(List, ListAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(System, SystemAdmin)
