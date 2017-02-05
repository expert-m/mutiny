from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'date_birth', 'education', 'tech_stack', 'about', 'gender',)
    list_display = ('user', 'date_birth', 'gender',)
    list_filter = ('date_birth', 'gender',)

admin.site.register(Profile, ProfileAdmin)
