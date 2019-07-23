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

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def number_of_followers(self):
        print(self.followers.count())
        if self.followers.count():
            return self.followers.count()
        else:
            return 0

    @classmethod
    def search_by_username(cls,search_word):
        get_search = cls.objects.filter(username__icontains=search_word)
        return get_search

    @property
    def image(self):
        if self.profile_path and hasattr(self.profile_path, 'url'):
            return self.profile_path.url


