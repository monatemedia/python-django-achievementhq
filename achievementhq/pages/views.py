from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def resume(request):
    return render(request, 'pages/resume.html')

def projects(request):
    return render(request, 'pages/projects.html')

def contact(request):
    return render(request, 'pages/contact.html')
