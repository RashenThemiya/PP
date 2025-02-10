from django.shortcuts import render
from .models import Skill, Project, Post
from django.core.paginator import Paginator
 # Make sure your Post model is imported

def posts(request):
    """Render the blog posts page with pagination."""
    post_list = Post.objects.all().order_by('-created_at')  # Fetch all posts and order by creation date
    paginator = Paginator(post_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get the posts for the current page
    return render(request, 'posts.html', {'page_obj': page_obj}) 


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
    return render(request, 'skills.html', {'range_100': range(100)})
# Ensure this matches your template file name

def projects(request):
    """Render the projects page."""
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})



def contact(request):
    """Render the contact page."""
    return render(request, 'contact.html')
