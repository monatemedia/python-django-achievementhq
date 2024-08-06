from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django.utils import timezone

# List all posts
@login_required
def index(request):
    posts = Post.objects.filter(user=request.user).order_by('-pub_date')
    user_joined_date = request.user.date_joined
    user_name = request.user.username
    current_year = timezone.now().year
    return render(request, 'posts/index.html', {
        'posts': posts,
        'user_joined_date': user_joined_date,
        'user_name': user_name,
        'current_year': current_year
    })

# Create a new post
@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.pub_date = timezone.now()
            post.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    return render(request, 'posts/form.html', {'form': form, 'title': 'Create Post'})

# Read a specific post
@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    return render(request, 'posts/detail.html', {'post': post})

# Update an existing post
@login_required
def update(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/form.html', {'form': form, 'title': 'Edit Post'})

# Delete a post
@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:index')
    return render(request, 'posts/confirm_delete.html', {'post': post})
