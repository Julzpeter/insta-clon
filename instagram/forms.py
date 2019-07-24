from django import forms
from .models import Profile, Image, Comment
from django.contrib.auth.models import User


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_path', 'bio']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'caption']


class CommentForm(forms.ModelForm):

    comment = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Add comment'}), label='')

    class Meta:
        model = Comment
        exclude = ('post', 'posted', 'user')
