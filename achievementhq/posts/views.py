from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm
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
    return render(request, 'posts/form.html', {
        'form': form,
        'title': 'Create Post',
        'is_editing': False,
    })

# Read a specific post
@login_required
def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    comments = Comment.objects.filter(post=post)
    return render(request, 'posts/detail.html', {
        'post': post,
        'comments': comments,
    })

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
    return render(request, 'posts/form.html', {
        'form': form,
        'title': 'Edit Post',
        'post': post,
        'is_editing': True,
    })

# Delete a post
@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('posts:index')
    return render(request, 'posts/confirm_delete.html', {'post': post})

# Create a new comment
@login_required
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.pub_date = timezone.now()
            comment.save()
            return redirect('posts:detail', post_id=post.id)
    else:
        form = CommentForm()
    return render(request, 'posts/comment_form.html', {
        'form': form,
        'post': post,
        'title': 'Add Comment',
    })

# Update an existing comment
@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'posts/comment_form.html', {
        'form': form,
        'post': comment.post,
        'title': 'Edit Comment',
    })

# Delete a comment
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user and request.user != comment.post.user:
        return redirect('posts:detail', post_id=comment.post.id)
    
    if request.method == 'POST':
        comment.delete()
        return redirect('posts:detail', post_id=comment.post.id)
    return render(request, 'posts/confirm_delete.html', {'post': comment.post})