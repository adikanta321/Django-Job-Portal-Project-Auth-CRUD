
## 📄 License

This project is licensed under the [MIT License](LICENSE).
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)



## 🧑‍💼 Python , Django Job Portal

A powerful, production-ready Job Portal built with Django — featuring secure custom authentication, robust email workflows, and a fully responsive interface.

This project demonstrates full-stack development using Django, with a focus on clean code architecture, real-world use cases, and seamless user experience. Users can register and log in via email, explore curated job listings, apply with a single click, and track their applications from a personalized dashboard.

Admins have complete control over job postings with full CRUD capabilities. The application features secure password reset via SMTP, one-click job applications, and a professional UI powered by Bootstrap 5 — making it an ideal showcase of professional Django development.

---

## ✨ Features

- ✅ Email-Based Authentication

 Secure and intuitive login system using email credentials, replacing Django's default username-based authentication.

- 🔐 Password Reset via Google SMTP

 Robust password recovery flow using Django’s token system with Gmail’s SMTP server via smtplib and Google App Passwords.

- 📄 Dynamic Job Listings with Detailed Views

 Job data is dynamically fetched from a MySQL database and rendered using Django’s ORM and templating engine.

- ⚡ One-Click Job Applications

-- Authenticated users can apply to jobs instantly, with their application data stored in relational tables without redundant forms.

- 🧾 User Dashboard for Applications

-- A personalized dashboard shows the list of jobs each user has applied for — powered by optimized database queries.

- 🗑️ Delete Applied Jobs

-- Users have the option to remove applications with confirmation prompts and backend integrity checks.

- 🛠️ Admin-Side Full Job Management (CRUD)

-- Admins can create, update, and delete job listings using Django Admin, with clean model registration and validation.

- 🖼️ Profile Picture Display in Navbar

-- Users can upload a profile picture stored in Django’s media folder, automatically rendered in the site’s top navigation.

- 📦 Database Architecture (MySQL)

-- All user data, job posts, applications, and media files are securely stored using a normalized MySQL schema with Django’s ORM handling complex relations.

- 💬 Interactive Flash Messages

-- All actions such as login, apply, update, and delete show appropriate success/error messages using Django’s messages framework.

- 📱 Responsive Frontend (Bootstrap 5)

-- Clean, modern, and mobile-first UI design using Bootstrap 5 for cross-device compatibility and a professional experience.



---

## 🛠 Tech Stack

- **Backend:** Python 3, Django 5
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Database:** MySQL (default, easily swappable with SQL)
- **Authentication:** Email login, secure password hashing
- **Email Service:** Google SMTP (App Password)
- **Deployment Ready:** Git + GitHub version control

---

## 🚀 Getting Started Locally

1. **Clone the Repository**
   ```bash
   git clone https://github.com/adikanta321/django-job-portal.git
   cd django-job-portal
