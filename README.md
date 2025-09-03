
## 📄 License

This project is licensed under the [MIT License](LICENSE).
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🧑‍💼 Python , Django Job Portal

A powerful, production-ready Job Portal built with Django — featuring secure custom authentication, robust email workflows, and a fully responsive interface.

This project demonstrates full-stack development using Django, with a focus on clean code architecture, real-world use cases, and seamless user experience. Users can register and log in via email, explore curated job listings, apply with a single click, and track their applications from a personalized dashboard.

Admins have complete control over job postings with full CRUD capabilities. The application features secure password reset via SMTP, one-click job applications, and a professional UI powered by Bootstrap 5 — making it an ideal showcase of professional Django development.

---
<img width="34" height="34" alt="icons8-linkedin-48" src="https://github.com/user-attachments/assets/9ba1e976-3dce-4d38-8d6a-673266855b5f" /> Linked-In : https://www.linkedin.com/in/dash-rudra/?originalSubdomain=in [Connect With Me]

## ✨ Features

- ✅ Email-Based Authentication
- ![Screenshot_15-8-2025_12380_127 0 0 1](https://github.com/user-attachments/assets/bf65ed9c-a74c-4836-a61b-7ad1a55c5085)

 Secure and intuitive login system using email credentials, replacing Django's default username-based authentication.


- 🔐 Password Reset via Google SMTP

 ![Screenshot_15-8-2025_123845_127 0 0 1](https://github.com/user-attachments/assets/e98c0cc6-a597-4591-a5fd-8014faca58b5)
  Robust password recovery flow using Django’s token system with Gmail’s SMTP server via smtplib and Google App Passwords.



- 📄 Dynamic Job Listings with Detailed Views

 ![Screenshot_3-Ui-Home Page View](https://github.com/user-attachments/assets/c6bde4a6-c1e5-4b96-baa8-95ea702e3c12)

  Job data is dynamically fetched from a MySQL database and rendered using Django’s ORM and templating engine.



- ⚡ One-Click Job Applications
![Screenshot_5-Applied_job View With CRUD-opr](https://github.com/user-attachments/assets/34219f55-95b1-44ce-a1f3-f85e47a0694e)
-- Authenticated users can apply to jobs instantly, with their application data stored in relational tables without redundant forms.


- 🧾 User Dashboard for Applications
- ![Screenshot_4-UI-DashBoard View-CRUD-opr](https://github.com/user-attachments/assets/d4389aeb-a72e-49be-8ef8-a1022a33560e)

-- A personalized dashboard shows the list of jobs each user has applied for — powered by optimized database queries.

- 🗑️ Delete Applied Jobs
![Screenshot_5-Applied_job View With CRUD-opr](https://github.com/user-attachments/assets/95a968e9-ce58-496f-983d-ce283e2e59a2)

-- Users have the option to remove applications with confirmation prompts and backend integrity checks.

- 🛠️ Admin-Side Full Job Management (CRUD)

-- Admins can create, update, and delete job listings using Django Admin, with clean model registration and validation.

- 🖼️ Profile Picture Display in Navbar
- ![Screenshot_4-UI-DashBoard View-CRUD-opr](https://github.com/user-attachments/assets/0b242eed-76c0-4261-9338-66a6331539a8)


-- Users can upload a profile picture stored in Django’s media folder, automatically rendered in the site’s top navigation.

- 📦 Database Architecture (MySQL)

-- All user data, job posts, applications, and media files are securely stored using a normalized MySQL schema with Django’s ORM handling complex relations.

- 💬 Interactive Flash Messages

-- All actions such as login, apply, update, and delete show appropriate success/error messages using Django’s messages framework.

- 📱 Responsive Frontend (Bootstrap 5)
- ![Screenshot_3-Ui-Home Page View](https://github.com/user-attachments/assets/7e068961-6d6f-4e30-aca3-74d1ef475682)
  
- Search View of Job Portal Website:
- ![Screenshot_1-Search-Filter View](https://github.com/user-attachments/assets/24852d2a-3074-422e-9964-2e22e87e07c9)
  
- Apply The Jobs:
![Screenshot_2-Search detail View](https://github.com/user-attachments/assets/7fcffe08-bd8d-4718-9453-725f2513908e)


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
