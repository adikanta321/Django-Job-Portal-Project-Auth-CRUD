from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    # Columns shown in the user list page (admin)
    list_display = (
        'id', 'email', 'full_name', 'phone_number', 'is_employer', 'is_verified', 'is_staff'
    )
    list_filter = ('is_employer', 'is_verified', 'is_staff', 'is_active')

    # Sections and fields displayed in user detail/edit page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {
            'fields': (
                'full_name', 'phone_number', 'profile_picture',
                'address', 'city', 'state', 'country', 'zip_code',
                'date_of_birth', 'bio'
            )
        }),
        (_('Professional Info'), {
            'fields': (
                'job_title', 'skills', 'linkedin_profile',
                'github_profile', 'projects', 'resume'
            )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'is_verified', 'is_employer', 'groups', 'user_permissions'
            )
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields used when creating a user from the admin panel
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2',
                'is_active', 'is_staff', 'is_verified', 'is_employer'
            ),
        }),
    )

    search_fields = ('email', 'full_name', 'phone_number')
    ordering = ('-date_joined',)
