from django.urls import path
from . import views
urlpatterns = [
    # Define URL patterns for user registration and login
    path('', views.home, name='home'),  # Home view

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # Add more paths as needed for other views
    path('forgot_password/', views.forgot_password_view, name='forgot_password'),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='reset_password'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('search/', views.search_view, name='search'),
    path('job_detail/<int:job_id>/', views.job_detail, name='job_detail'),


]
