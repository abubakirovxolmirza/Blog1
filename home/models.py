from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} Profile"


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.CharField(max_length=130)
    content = models.TextField()
    image = models.ImageField(upload_to="profile_pics", blank=True, null=True)
    dateTime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_blog_posts')

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f"{self.author.username} - Blog Title: {self.title}"

    def get_absolute_url(self):
        return reverse('blogs')


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    dateTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - Comment: {self.content}"