from django.contrib import admin
from .models import *

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'job_title', 'company_name', 'job_type', 'job_location', 'salary', 'posted_date')
    search_fields = ('job_title', 'company_name', 'job_location')
    list_filter = ('job_type', 'posted_date')
    ordering = ('-posted_date',)
    date_hierarchy = 'posted_date'
    readonly_fields = ('posted_date',)
    
    fieldsets = (
        (None, {
            'fields': (
                'job_title',
                'company_name',
                'job_type',
                'job_description',
                'job_location',
                'salary',
                'application_deadline',
                'company_logo'
            )
        }),
    )



@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'user', 'application_date')  # ✅ updated fields
    search_fields = ('job__job_title', 'user__email')  # You can search by related fields like this
    list_filter = ('application_date',)