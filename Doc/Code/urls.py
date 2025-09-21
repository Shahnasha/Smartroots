from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome, name='welcome'),
    path('about/', views.about_page, name='about'),
    path('parent-login/', views.parent_login, name='parent_login'),
    path('child-login/', views.child_login, name='child_login'),
    path('parent-dashboard/', views.parent_dashboard, name='parent_dashboard'),
    path('submit-ratings/', views.submit_ratings, name='submit_ratings'),
    path('mark-complete/<int:activity_id>/', views.mark_activity_complete, name='mark_activity_complete'),
     path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]
