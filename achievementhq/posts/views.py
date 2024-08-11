from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Correct import for User model
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone

# List all users by latest post
@login_required
def user_list(request):
    users = User.objects.all()
    user_data = []

    for user in users:
        latest_post = Post.objects.filter(user=user).order_by('-pub_date').first()
        user_data.append({
            'id': user.id,
            'username': user.username,
            'latest_post_title': latest_post.heading_text if latest_post else 'No posts',
            'latest_post_message': latest_post.message_text if latest_post else 'No content available',
            'latest_post_date': latest_post.pub_date if latest_post else timezone.make_aware(timezone.datetime.min)
        })

    # Sort user_data by latest_post_date in descending order
    user_data.sort(key=lambda x: x['latest_post_date'], reverse=True)

    return render(request, 'posts/user_list.html', {'user_data': user_data})

@login_required
def index(request, user_id=None):
    try:
        if user_id:
            user = get_object_or_404(User, id=user_id)
            posts = Post.objects.filter(user=user).order_by('-pub_date')
            user_name = user.username
            user_joined_date = user.date_joined
            user_owns_posts = user == request.user
        else:
            posts = Post.objects.filter(user=request.user).order_by('-pub_date')
            user_name = request.user.username
            user_joined_date = request.user.date_joined
            user_owns_posts = True
    except User.DoesNotExist:
        raise Http404("User does not exist")

    return render(request, 'posts/index.html', {
        'posts': posts,
        'user_joined_date': user_joined_date,
        'user_name': user_name,
        'user_id': user_id,
        'user_owns_posts': user_owns_posts,
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
    try:
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post=post).order_by('-pub_date')
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    return render(request, 'posts/detail.html', {
        'post': post,
        'comments': comments,
    })

# Update an existing post
@login_required
def update(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id, user=request.user)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
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
    try:
        post = get_object_or_404(Post, id=post_id, user=request.user)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
    if request.method == 'POST':
        post.delete()
        return redirect('posts:index')
    return render(request, 'posts/confirm_delete.html', {'post': post})

# Create a new comment
@login_required
def create_comment(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")
    
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

# Displaying a single comment
@login_required
def comment_detail(request, comment_id):
    try:
        comment = get_object_or_404(Comment, id=comment_id)
    except Comment.DoesNotExist:
        raise Http404("Comment does not exist")

    context = {
        'title': 'Comment Details',
        'subtitle': 'Comment by {}'.format(comment.user.username),
        'comment': comment,
    }
    return render(request, 'posts/comment_detail.html', context)


# Update an existing comment
@login_required
def update_comment(request, comment_id):
    try:
        comment = get_object_or_404(Comment, id=comment_id)
        print(f"Fetched comment: {comment}")
    except Comment.DoesNotExist:
        print(f"No comment found with id: {comment_id}")
        raise Http404("No Comment matches the given query.")
    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    
    context = {
        'title': 'Edit Comment',
        'subtitle': 'Update your comment below:',
        'form': form,
        'post': comment.post
    }
    
    return render(request, 'posts/comment_form.html', context)

# Delete a comment
@login_required
def delete_comment(request, comment_id):
    # Fetch the comment object or return a 404 error if it does not exist
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user has permission to delete the comment
    if request.user != comment.user and request.user != comment.post.user:
        return redirect('posts:detail', post_id=comment.post.id)

    # Handle POST request for deletion
    if request.method == 'POST':
        comment.delete()
        # Redirect to the post detail page after deletion
        return redirect('posts:detail', post_id=comment.post.id)

    # Render the confirmation page if the request method is not POST
    return render(request, 'posts/confirm_delete.html', {'post': comment.post, 'comment': comment})

# Confirm delete for posts and comments
@login_required
def confirm_delete(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        comment_id = request.POST.get('comment_id')

        if post_id:
            post = get_object_or_404(Post, id=post_id)
            post.delete()
            return redirect('posts:index')
        elif comment_id:
            comment = get_object_or_404(Comment, id=comment_id)
            post_id = comment.post.id  # Get the post ID related to the comment
            comment.delete()
            return redirect('posts:detail', post_id=post_id)  # Redirect to the post detail page

    # If GET request or missing IDs, show the confirmation page
    post_id = request.GET.get('post_id')
    comment_id = request.GET.get('comment_id')

    context = {}
    if post_id:
        context['post'] = get_object_or_404(Post, id=post_id)
    elif comment_id:
        context['comment'] = get_object_or_404(Comment, id=comment_id)
        context['post_id'] = context['comment'].post.id  # Pass the post ID for cancellation

    return render(request, 'posts/confirm_delete.html', context)
