
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment,Likes
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .forms import ProfileForm, ImageForm, CommentForm

# Create your views here.
@login_required
def home(request):
    form = CommentForm()
    images = Image.objects.all().order_by('-image_created')
    users = User.objects.all()
    current = request.user
    comments = Comment.objects.all().order_by('-posted')
    likes = Likes.objects.all().count()
   
    return render(request, 'index.html', {"images": images, "users": users, 'user': current, "form": form, 'comments': comments})


def get_search(request):
    profile = Profile.objects.all
    print(profile)
    if 'user' in request.GET and request.GET["user"]:
        search_word = request.GET.get("user")
        print(search_word)
        searched_users = User.objects.filter(username__icontains=search_word)
        print(searched_users)
        message = f"{search_word}"

        return render(request, 'search.html', {"message": message, "users": searched_users, "profile": profile})

    else:
        message = "You haven't searched for anyone"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def profile(request, id):
    user = User.objects.get(id=id)
    current_user = request.user
    images = Image.objects.filter(editor_id=id)

    try:
        profile = Profile.objects.get(user_id=id)
    except ObjectDoesNotExist:
        return redirect(update_profile, current_user.id)
    else:

        return render(request, 'profile.html', {"user": user, "images": images, "profile": profile})


@login_required(login_url='/accounts/login/')
def update_profile(request, id):
    current_user = request.user
    user = User.objects.get(id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user_id = id
            profile.save()
        return redirect(home)

    else:
        form = ProfileForm()
    return render(request, 'update_profile.html', {"user": user, "form": form})


@login_required(login_url='/accounts/login/')
def post_image(request, id):
    current_user = request.user
    current_profile = Profile.objects.get(user_id=id)
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.user_profile = current_profile
            image.save()
        return redirect(home)

    else:
        form = ImageForm()
    return render(request, 'post_image.html', {"user": current_user, "form": form})


@login_required(login_url='/accounts/login/')
def post_comment(request, image_id):
    comments = Comment.objects.filter(post_id=image_id)
    current_user = request.user
    current_image = Image.objects.get(id=image_id)
    try:
        likes = Likes.object.filter(image_id).count()
    except ObjectDoesNotExist:
        likes = 0
    try:
        like = Likes.objects.filter(
            image_id=image_id).get(user_id=request.user)
    except ObjectDoesNotExist:
        like = 0
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = current_image
            comment.user = current_user
            comment.save()
            print(comments)
            return redirect(home)
    else:
        form = CommentForm()

    return render(request, 'comments.html', {"form": form, 'comments': comments, "image": current_image, "user": current_user, 'like': like, "likes": likes})

def like_pic(request,pic_id):
    current_user = request.user
    image = Image.objects.get(id=pic_id)
    new_like = Likes(post=image, user=current_user)
    new_like.save()
    return redirect(home, image.id)
   




def signout(request):
    logout(request)
    return redirect('login')



