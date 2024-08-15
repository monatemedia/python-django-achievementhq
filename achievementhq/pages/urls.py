from django.urls import path

from . import views

app_name = 'pages'
urlpatterns = [
    path('', views.index, name='index'),
    path('why-join', views.why_join, name='why-join'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]