# jobs/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Job, JobApplication

@login_required
def job_list(request):
    jobs = Job.objects.all().order_by('-posted_date')
    # This is ALREADY CORRECT - values_list('job_id', flat=True) uses your actual PK field
    applied_jobs = JobApplication.objects.filter(user=request.user).values_list('job_id', flat=True) 
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'applied_jobs': applied_jobs})

@login_required
def apply_job(request, job_id):
    # This is CORRECT, pk refers to the primary key regardless of its name (job_id in this case)
    job = get_object_or_404(Job, pk=job_id) 

    already_applied = JobApplication.objects.filter(job=job, user=request.user).exists()
    if already_applied:
        messages.warning(request, "You have already applied for this job.")
    else:
        JobApplication.objects.create(job=job, user=request.user)
        messages.success(request, "You have successfully applied for this job.")

    return redirect('home')


@login_required
def view_applied_jobs(request):
    user = request.user
    print("Logged in user:", user.email, "| ID:", user.id)

    applications = JobApplication.objects.filter(user=request.user, job__isnull=False).select_related('job')

    print("Applications count (after job__isnull filter):", applications.count())

    if applications.exists():
        for app in applications:
            print(f"  --- Application ID: {app.id} ---")
            print(f"  Job object linked: {app.job}")
            print(f"  Job ID (app.job.job_id): {app.job.job_id if app.job else 'N/A (job is None)'}") 
            print(f"  Job Title: {app.job.job_title if app.job else 'N/A (job is None)'}")
            print(f"  Job Company: {app.job.company_name if app.job else 'N/A (job is None)'}")
            print(f"  Type of app.job.job_id: {type(app.job.job_id) if app.job and app.job.job_id else 'N/A'}")
    else:
        print("  No applications found for this user after filtering.")

    return render(request, 'applied_jobs.html', {'applications': applications})


@login_required
def delete_job(request, job_id):
    try:
        application = get_object_or_404(JobApplication, job_id=job_id, user=request.user)
    except JobApplication.DoesNotExist:
        messages.error(request, "The application you tried to remove was not found or already deleted.")
        return redirect('applied-jobs') # Always return here

    # This block handles the POST request for deletion
    if request.method == "POST":
        application.delete()
        messages.success(request, "You have removed your application for this job.")
        return redirect('applied-jobs') # Always return here

    # This block handles any other request method (e.g., GET requests directly to this URL)
    # Since deletion should only happen via POST, for GET requests, we just redirect.
    messages.warning(request, "Invalid request method for deleting an application.")
    return redirect('applied-jobs') # Ensure a redirect is always returned