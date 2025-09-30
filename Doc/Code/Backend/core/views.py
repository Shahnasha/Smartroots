from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Activity, Progress
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required

@login_required
def undo_activity_complete(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    Progress.objects.filter(user=request.user, activity=activity).delete()
    messages.success(request, "❌ Activity unmarked successfully.")
    return redirect('child_dashboard')

def welcome(request):
    return render(request, 'welcome.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def test_background(request):
    return render(request, 'test_background.html')

def about_page(request):
    return render(request, 'about.html')


# 🧒 Child Dashboard
# 🧒 Child Dashboard
def child_dashboard(request):
    if request.user.is_authenticated:
        progress = Progress.objects.filter(user=request.user).select_related('activity')
        completed_count = progress.count()
        total_count = Activity.objects.filter(is_active=True).count()
        percent_complete = int((completed_count / total_count) * 100) if total_count > 0 else 0

        # 🏅 Milestone Badges
        badges = []
        if completed_count >= 1:
            badges.append("🌱 First Activity Done")
        if completed_count >= 5:
            badges.append("🎯 5 Activities Completed")
        if completed_count >= 10:
            badges.append("🏆 10 Activities Completed")

        return render(request, 'child_dashboard.html', {
            'progress': progress,
            'completed_count': completed_count,
            'total_count': total_count,
            'percent_complete': percent_complete,
            'badges': badges
        })
    return redirect('child_login')




# 🧒 Child Login
def child_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('child_dashboard')
        messages.error(request, 'Oops! That name or code didn’t work.')
    return render(request, 'child_login.html')


# 👨‍👩‍👧 Parent Login
def parent_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('parent_dashboard')
        messages.error(request, 'Invalid username or password.')
    return render(request, 'parent_login.html')

# 🧭 Parent Dashboard
def parent_dashboard(request):
    age_range = range(3, 11)
    skill_range = range(1, 6)
    skill_names = [
        ("speaking", "Speaking"),
        ("listening", "Listening"),
        ("reading", "Reading"),
        ("writing", "Writing"),
        ("drawing", "Drawing"),
        ("moving", "Moving"),
        ("playing_with_others", "Playing with Others")
    ]
    return render(request, 'parent_dashboard.html', {
        'age_range': age_range,
        'skill_range': skill_range,
        'skill_names': skill_names
    })



def submit_ratings(request):
    if request.method == 'POST':
        # Collect ratings and filters
        skill_ratings = {
            "speaking": int(request.POST.get('speaking', 0)),
            "listening": int(request.POST.get('listening', 0)),
            "reading": int(request.POST.get('reading', 0)),
            "writing": int(request.POST.get('writing', 0)),
            "drawing": int(request.POST.get('drawing', 0)),
            "moving": int(request.POST.get('moving', 0)),
            "playing with others": int(request.POST.get('playing_with_others', 0))
        }
        age = int(request.POST.get('age', 0))
        difficulty = int(request.POST.get('difficulty', 0))
        activity_type = request.POST.get('activity_type', 'all')

        # Filter activities
        recommendations = []
        all_activities = Activity.objects.filter(is_active=True)

        for activity in all_activities:
            skill_match = abs(activity.level - skill_ratings.get(activity.type, 0)) <= 1
            difficulty_match = abs(activity.level - difficulty) <= 1
            age_match = activity.min_age <= age <= activity.max_age

            if skill_match and difficulty_match and age_match:
                if activity_type == 'all' or activity.type == activity_type:
                    recommendations.append(activity)

        return render(request, 'recommendations.html', {
            'recommendations': recommendations,
            'activity_type': activity_type
        })

def mark_activity_complete(request, activity_id):
    activity = get_object_or_404(Activity, id=activity_id)
    Progress.objects.get_or_create(user=request.user, activity=activity)
    messages.success(request, "✅ Activity marked as complete!")
    return redirect('child_dashboard')

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            messages.success(request, "✅ Your feedback was submitted successfully! Thank you for helping SmartRoots grow.")
            return redirect('parent_dashboard')
    else:
        form = FeedbackForm()
    return render(request, 'submit_feedback.html', {'form': form})





