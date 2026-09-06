from django.shortcuts import render, get_object_or_404
from .models import Blog

def home(request):
    return render(request, 'main/index.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'main/blogs.html', {'blogs': blogs})

def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'main/details.html', {'blog': blog})