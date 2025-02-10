from django.db import models

# Updated Skill Model (Added Logo)
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField()  # Percentage (0-100)
    logo = models.ImageField(upload_to="skills/", blank=True, null=True)  # Skill Logo

    def __str__(self):
        return self.name

# Updated Project Model (Added Video Upload)
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    video = models.FileField(upload_to="projects/videos/", blank=True, null=True)  # Video Upload
    github_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="posts/files/", blank=True, null=True)  # For PDF, ZIP, or presentation files

    def __str__(self):
        return self.title
