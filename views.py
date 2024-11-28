# personal/views.py
from django.shortcuts import render

def about_view(request):
    return render(request, 'personal/about.html')

def hobbies_view(request):
    return render(request, 'personal/hobbies.html')

def projects_view(request):
    return render(request, 'personal/projects.html')
