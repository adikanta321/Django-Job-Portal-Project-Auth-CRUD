# jobs/urls.py
from django.urls import path
from .views import *

urlpatterns = [
  path('',job_list, name='job_list'),
  path('apply/<int:job_id>/', apply_job, name='apply_job'),
  path('applied-jobs/', view_applied_jobs, name='applied-jobs'),
  path('applied/delete/<int:job_id>/',delete_job,name='delete_applied_job')
]