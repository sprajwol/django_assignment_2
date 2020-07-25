from django.db import models
from datetime import date, datetime

from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="Blog View")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, null=True, blank=True)
    main_img = models.ImageField(
        upload_to='uploads/blog_imgs/title/', blank=True)
    body = models.TextField(blank=True, null=True)
    snippet = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title) + ' | ' + str(self.author.first_name) + ' ' + str(self.author.last_name)
