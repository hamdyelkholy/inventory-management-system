from django.shortcuts import render, redirect
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>hello to my website</h1>")

def data(request):
    students = ['Hamdy', 'Ahmed', 'Mohamed', 'Omar', 'Youssef']
    return render(request, 'data.html', {'students': students})

def about(request):
    return HttpResponse("<h1>about page from request</h1>")

def redirect_about(request):
    return redirect('about')