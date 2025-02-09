from django.shortcuts import render
from .models import Skill, Project, Post

def home(request):
    """Render the home page with skills, projects, and blog posts."""
    skills = Skill.objects.all()
    projects = Project.objects.all()
    posts = Post.objects.all()
    return render(request, 'main/home.html', {'skills': skills, 'projects': projects, 'posts': posts})

def profile(request):
    """Render the profile page with skills, projects, and blog posts."""
    skills = Skill.objects.all()
    projects = Project.objects.all()
    posts = Post.objects.all()
    return render(request, 'profile.html', {'skills': skills, 'projects': projects, 'posts': posts})

def skills(request):
    """Render the skills page."""
    skills = Skill.objects.all()
    return render(request, 'skills.html', {'skills': skills})

def projects(request):
    """Render the projects page."""
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def posts(request):
    """Render the blog posts page."""
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def contact(request):
    """Render the contact page."""
    return render(request, 'contact.html')
