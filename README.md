SmartRoots is a family-focused learning platform designed to help parents nurture their children's growth through personalized, skill-based activities. Built with Django and developed using Visual Studio Code, SmartRoots offers a dynamic, database-driven experience where parents and children can log in through separate dashboards, explore curated activities filtered by age, skill, and difficulty, and track progress over time. The platform replaces hardcoded logic with admin-controlled models, allowing for flexible content management and personalized recommendations based on user ratings.

Introduction
This system is built to automate the delivery of age-appropriate, skill-targeted activities for children. Using a database of curated content and a rating-based recommendation engine, SmartRoots helps parents discover meaningful learning experiences tailored to their child’s development. The platform includes a warm admin dashboard for content management, separate login flows for parents and children, and a simple frontend for interaction.

SmartRoots is ideal for educational use, prototyping, or as the foundation for a full-scale learning platform. It showcases how thoughtful branding, emotional design, and backend logic can work together to create a nurturing digital space.

Features
Django backend with models for activities, users, ratings, and progress

Admin interface for adding/editing activities and managing users

Parent dashboard for tracking child progress and rating activities

Child dashboard for viewing and completing activities

Basic frontend with nurturing design and intuitive navigation

Developed and debugged using Visual Studio Code for efficient workflow

Recommendation System
Uses Django ORM queries to filter activities by age, skill, and difficulty

Ratings influence future recommendations

Activities stored in database for dynamic retrieval

System can be extended with machine learning for smarter suggestions

Technology Stack
Backend: Python, Django

Frontend: Django templates (HTML/CSS), optional JavaScript

Database: SQLite (default, can be upgraded)

Admin: Django admin panel

IDE: Visual Studio Code

Design: Custom branding, nurturing backgrounds, gradient overlays

Data Flow
Parent or child logs in via dedicated dashboard

User views recommended activities based on filters and ratings

Activity is completed and rated

Rating updates database and influences future suggestions

Admin can view all users, activities, and progress

Setup Instructions
Clone the repository:

bash
git clone <your-repo-url>  
cd smartroots  
Open the project in Visual Studio Code:

bash
code .  
Create and activate a Python virtual environment:

bash
python -m venv venv  
.\venv\Scripts\activate  
Install dependencies:

bash
pip install -r requirements.txt  
Run migrations:

bash
python manage.py makemigrations  
python manage.py migrate  
Create a superuser for admin access:

bash
python manage.py createsuperuser  
Start the development server:

bash
python manage.py runserver  
Access the application:

Frontend: http://127.0.0.1:8000/

Admin panel: http://127.0.0.1:8000/admin/

Project Structure
Code
smartroots/               - Django project settings  
activities/               - App for activity logic and recommendations  
users/                    - App for parent/child login and profiles  
templates/                - HTML templates for frontend  
static/                   - CSS, JS, and image assets  
requirements.txt          - Python dependencies  
.github/copilot-instructions.md - Project automation checklist  
Usage Notes
Admins can add new activities and manage user accounts

Parents can rate activities and track child progress

The recommendation engine is based on database queries and can be enhanced later

Next Steps
Add user registration and authentication

Improve frontend UI with animations and responsive design

Introduce progress badges and gamification

Expand activity categories and filters

Add multilingual support for broader accessibility
