from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('username', 'email')
    search_field = ('username', 'email')
    list_per_page = 25

admin.site.register(User, UserAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    search_field = ('user')
    list_per_page = 25

admin.site.register(Profile, ProfileAdmin)
