from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import City, District, Institution, Process, CustomUser

# City Admin
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

# District Admin
@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    list_filter = ('city',)
    search_fields = ('name', 'city__name')
    list_per_page = 20

# Institution Admin
@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'district', 'phone', 'email')
    list_filter = ('city', 'district')
    search_fields = ('name', 'city__name', 'district__name')
    list_per_page = 20

# Process Admin
@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'district')
    list_filter = ('city', 'district')
    search_fields = ('name', 'city__name', 'district__name')
    list_per_page = 20

# CustomUser Admin
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'city', 'district', 'is_staff')
    list_filter = ('city', 'district', 'is_staff')
    search_fields = ('username', 'email', 'city__name', 'district__name')
    list_per_page = 20

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'city', 'district')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'city', 'district', 'is_staff', 'is_active'),
        }),
    )