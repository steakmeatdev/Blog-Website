from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import *


from rest_framework import viewsets
from .serializers import model_Serializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
## For this home page, being logged in is required
@login_required(login_url="/login")
def home(request):

    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        
        ## According to chatGPT, I can use either use this or use the simpler get method with try and catch and then just delete
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()

    return render(request, "main/home.html", {"posts": posts})

@login_required(login_url="/login")
def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect("/home")
        else:
            print(form.errors)
            form = PostForm()
    return render(request, "main/create_post.html", {"form": form})

def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/home")
    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {"form": form})

## Must add this function because logout wasn't working for some reason

def auth_logout(request):
    logout(request)
    return redirect('home')

## Using serializers

## This BlogPostViewSet class will automatically provide list, create, retrieve, update, and destroy actions
## ican override action methods like create(), update(), or destroy() to add custom logic.
class model_ViewSet(viewsets.ModelViewSet):
    queryset = model_.objects.all()  # Use descriptive model name
    serializer_class = model_Serializer  # Assuming you have a corresponding serializer

    # ... existing code ...

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        blog_post = self.get_object()  # Avoid overwriting the model reference
        # Add logic to like the blog post (e.g., incrementing a like count)
        return Response({'status': 'blog post liked'})