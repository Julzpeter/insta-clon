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

    def number_of_following(self):
        if self.following.count():
            return self.following.count()
        else:
            return 0

    @classmethod
    def search_by_username(cls, search_word):
        get_search = cls.objects.filter(username__icontains=search_word)
        return get_search

    @property
    def image(self):
        if self.profile_path and hasattr(self.profile_path, 'url'):
            return self.profile_path.url

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, null=True)
    image_created = models.DateTimeField(auto_now=True, auto_now_add=False)
    caption = models.CharField(max_length=220, default="")
    editor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="cm")
    user_profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item

    @classmethod
    def get_image_by_id(cls, id):
        fetched_image = cls.objects.get(id=id)
        return fetched_image

    @classmethod
    def update_image(cls, current_value, new_value):
        fetched_object = Image.objects.filter(
            editor=current_value).update(editor=new_value)
        return fetched_object


class Comment(models.Model):
    post = models.ForeignKey('Image', null=True)
    comment = models.CharField(max_length=300)
    posted = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.comment


