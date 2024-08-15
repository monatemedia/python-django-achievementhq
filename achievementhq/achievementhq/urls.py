"""
URL configuration for achievementhq project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # Include pages routes
    path('', include('pages.urls')),
    # Include polls routes
    path('polls/', include('polls.urls')),
    # Include users routes for login, register, and logout
    path('', include('users.urls')),
    # Include posts routes
    path('posts/', include('posts.urls')),
    path('admin/', admin.site.urls),
]

def page_not_found(request, exception):
    return render(request, '404.html', status=404)

def server_error(request):
    return render(request, '500.html', status=500)

handler404 = page_not_found
handler500 = server_error

# Serving static files during development
# if not settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)