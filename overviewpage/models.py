from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):

    POST_TYPE_CHOICES = (("0", "General"), ("1", "Armor Concepts"), ("2", "Portraits"), ("3", "Character Design"),)

    title = models.CharField(max_length=100)
    image = models.FileField(null=True, blank=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE) #if user is deleted, delete post as well.
    PostCategory = models.CharField(max_length = 20, choices = POST_TYPE_CHOICES, default = '0')

    def post_districtList(self):
        return dict(Post.POST_TYPE_CHOICES)[self.PostCategory]
