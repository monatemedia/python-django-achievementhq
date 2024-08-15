from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def why_join(request):
    return render(request, 'pages/why_join.html')

def contact(request):
    return render(request, 'pages/contact.html')
