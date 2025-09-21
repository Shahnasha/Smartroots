from django.contrib import admin
from django.urls import path
from core import views  # or your app name if different

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('about/', views.about_page, name='about'),  # ✅ Make sure this ends with a comma
    path('parent-login/', views.parent_login, name='parent_login'),
    path('child-login/', views.child_login, name='child_login'),
    path('parent-dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('child-dashboard/', views.child_dashboard, name='child_dashboard'),
    path('submit-ratings/', views.submit_ratings, name='submit_ratings'),
    path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
    path('admin/', admin.site.urls),

]
