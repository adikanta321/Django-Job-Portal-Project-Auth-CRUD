from django.db import models
from django.conf import settings

# Create your models here.
class Job(models.Model):
    JOB_TYPES = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'), 
        ('Contract', 'Contract'),
        ('Temporary', 'Temporary'), 
        ('Internship','Internship'),
        ('Remote','Remote'),
    )
    company_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    job_id = models.AutoField(primary_key=True)
    job_type = models.CharField(max_length=20, choices=JOB_TYPES, default='Full Time')
    job_description = models.TextField()
    job_location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateTimeField(null=True, blank=True)
    company_logo = models.ImageField(upload_to='company_logos/', null=True, blank=True)

    def __str__(self):
        return f"{self.job_title} at {self.company_name} ({self.job_type})"
    
class JobApplication(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)  # Optional now
    application_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'user')  # Prevent double apply

    def __str__(self):
        return f"{self.user.email} applied to {self.job.job_title}"