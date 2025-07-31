from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, UserLoginForm
from .forms import *
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.utils.encoding import force_str
from django.contrib.auth.tokens import default_token_generator
from jobs.models import *
from django.db.models import Q  # For complex queries

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


from django.contrib.auth import get_user_model
User = get_user_model()


# accounts/views.py

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # will later redirect to dashboard
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})

from jobs.models import Job

from django.shortcuts import render
from jobs.models import Job, JobApplication

from django.shortcuts import render
from jobs.models import Job, JobApplication

def home(request):
    jobs = Job.objects.all()
    applied_jobs = []

    if request.user.is_authenticated:
        applied_jobs = list(JobApplication.objects.filter(user=request.user).values_list('job__job_id', flat=True))

    return render(request, 'home.html', {
        'jobs': jobs,
        'applied_jobs': applied_jobs
    })




def logout_view(request):
    logout(request)
    return redirect('login')

def forgot_password_view(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset_link = request.build_absolute_uri(f'/reset_password/{uid}/{token}/')

                subject = "Reset Your Password"
                message = render_to_string(
                    'accounts/password_reset_email.html',
                    {'reset_link': reset_link, 'user': user
                     })
                email_msg = EmailMessage(
                    subject, message, to=[email]
                )
                email_msg.content_subtype = 'html'
                email_msg.send()

                messages.success(
                    request, "Password reset link has been sent to your email. ✅"
                )
                return redirect('login')
            except User.DoesNotExist:
                messages.error(
                    request, "No user found with this email address. ❌"
                )
    else:
        form = ForgotPasswordForm()
    return render(request, 'accounts/forgot_password.html', {'form': form})



def reset_password(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = ResetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Password reset successfully! You can now login.")
                return redirect('login')
        else:
            form = ResetPasswordForm(user)
        return render(request, 'accounts/set_new_password.html', {'form': form})
    else:
        messages.error(request, "Reset link is invalid or expired.")
        return redirect('forgot_password')

@login_required
def dashboard_view(request):
    return render(request, 'accounts/dashboard.html')

@login_required
def edit_profile_view(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully! ✅")
            return redirect('dashboard')
    else:
        form = EditProfileForm(instance=user)
    return render(request, 'accounts/edit_profile.html', {'form': form})


def search_view(request):
    """
    Handles search queries and displays matching jobs.
    """
    query = request.GET.get('q', '')
    jobs = []
    
    if query:
        search_query = (
            Q(job_title__icontains=query) |
            Q(job_description__icontains=query) |
            Q(company_name__icontains=query) |
            Q(job_location__icontains=query)
        )
        
        # Filter the jobs
        raw_jobs = Job.objects.filter(search_query)

        # Iterate over the raw queryset and only add jobs with a valid ID
        for job in raw_jobs:
            # CORRECTED: use job.job_id instead of job.id
            if job.job_id:
                jobs.append(job)
            else:
                print(f"DEBUG: Found a job without a job_id: {job}")

    context = {
        'jobs': jobs,
        'query': query,
    }

    return render(request, 'accounts/search_results.html', context)

def job_detail(request, job_id):
    """
    Displays the details of a single job.
    """
    # CORRECTED: get_object_or_404 now uses the correct primary key field 'job_id'
    job = get_object_or_404(Job, job_id=job_id)

    context = {
        'job': job,
    }

    return render(request, 'accounts/job_detail.html', context)