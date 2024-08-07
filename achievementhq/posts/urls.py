from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    # Post URLs
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('<int:post_id>/edit/', views.update, name='update'),
    path('<int:post_id>/delete/', views.delete, name='delete'),
    # Comment URLs
    path('posts/<int:post_id>/comments/create/', views.create_comment, name='create_comment'),
    path('comments/<int:comment_id>/edit/', views.update_comment, name='update_comment'),
    path('comments/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:post_id>/', views.detail, name='detail'),
    # User URLs
    path('user_list/', views.user_list, name='user_list'),  # This should match the URL you want
    path('user/<int:user_id>/', views.index, name='user_index'),
]
