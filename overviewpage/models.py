from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):

    POST_TYPE_CHOICES = (("0", "General"), ("1", "Armor Concepts"), ("2", "Portraits"), ("3", "Character Design"), ("4", "Posters"),)

    title = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE) #if user is deleted, delete post as well.
    PostCategory = models.CharField(max_length = 20, choices = POST_TYPE_CHOICES, default = '0')

    def post_districtList(self):
        return dict(Post.POST_TYPE_CHOICES)[self.PostCategory]

    def __str__(self):
        return self.title

class Project(models.Model):

    PROJECT_TYPE_CHOICES = (("0", "Apartment Website"), ("1", "Cosmonaut Game"), ("2", "This Website"),)

    project_title = models.CharField(max_length=100, default='PLACEHOLDER')
    title = models.CharField(max_length=100, default='PLACEHOLDER')
    title_highlight = models.CharField(max_length=100, default='PLACEHOLDER')
    image_first = models.FileField(null=True, blank=True)
    image_secondary = models.FileField(null = True, blank=True)
    subtitle_first = models.CharField(max_length=100, default='PLACEHOLDER')
    subtitle_second = models.CharField(max_length=100, default='PLACEHOLDER')
    description_first = models.TextField()
    description_second = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE) #if user is deleted, delete post as well.
    ProjectCategory = models.CharField(max_length = 20, choices = PROJECT_TYPE_CHOICES, default = '0')

    def post_districtList(self):
        return dict(Project.PROJECT_TYPE_CHOICES)[self.ProjectCategory]

    def __str__(self):
        return self.project_title

