from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from .models import Blog
from .forms import RegisterForm, BlogCreateForm, BlogModelForm

def home(request):
    return render(request, 'home.html')

def blogs(request):
    all_blogs = Blog.objects.all()
    return render(request, 'blogs.html', {'blogs': all_blogs})

def blog_detail(request, id):
    single_blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog_detail.html', {'blog': single_blog})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blogs')
    else:
        form = RegisterForm()
    return render(request, 'regester.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blogs')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def user_profile(request, username):
    profile_user = get_object_or_404(User, username=username)
    user_blogs = Blog.objects.filter(author=profile_user)
    return render(request, 'profile.html', {'profile_user': profile_user, 'blogs': user_blogs})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogCreateForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blogs')
    else:
        form = BlogCreateForm()
    return render(request, 'create_blog.html', {'form': form})

@login_required
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.author != request.user:
        return HttpResponseForbidden("Forbidden")
    
    if request.method == 'POST':
        form = BlogModelForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', id=blog.id)
    else:
        form = BlogModelForm(instance=blog)
    return render(request, 'edit_blog.html', {'form': form, 'blog': blog})

@login_required
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    if blog.author != request.user:
        return HttpResponseForbidden("Forbidden")
    
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs')
    return render(request, 'delete_confirm.html', {'blog': blog})