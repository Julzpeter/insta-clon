from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):

    profile_path = models.ImageField(
        upload_to='images/', default='images/juliet.jpg')
    bio = models.TextField()
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    followers = models.ManyToManyField(
        'Profile', related_name="followers_profile", blank=True)
    following = models.ManyToManyField(
        'Profile', related_name="following_profile", blank=True)


