from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Correct import for User model
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.utils import timezone

# List all users by latest post
@login_required
def user_list(request):
    try:
        users = User.objects.all()
        if not users:
            messages.warning(request, "No users found.")
            return render(request, 'posts/user_list.html', {'user_data': []})

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

    except Exception as e:
        # Log the error, then show a generic error message
        messages.error(request, "An error occurred while fetching users. Please try again later.")
        return render(request, 'posts/user_list.html', {'user_data': []})

# List all user posts
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

        # Show the message only if the user is viewing another user's index and no posts are found
        if not posts.exists() and not user_owns_posts:
            messages.info(request, "This user has not created any posts yet.")

        return render(request, 'posts/index.html', {
            'posts': posts,
            'user_joined_date': user_joined_date,
            'user_name': user_name,
            'user_id': user_id,
            'user_owns_posts': user_owns_posts,
        })

    except Exception as e:
        # Log the error (in a real app)
        messages.error(request, "An error occurred while fetching posts. You have been redirected back to the members area.")
        return redirect('posts:user_list')  # Redirect to the user list

# Create a new post
@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            try:
                post = form.save(commit=False)
                post.user = request.user
                post.pub_date = timezone.now()
                post.save()
                messages.success(request, "Your post has been successfully created.")
                return redirect('posts:index')  # Redirect to the user's own post index
            except Exception as e:
                # Log the error (in a real app)
                messages.error(request, "An error occurred while saving your post. Please try again.")
        else:
            messages.error(request, "Please correct the errors below.")
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

        if not comments.exists():
            messages.info(request, "Be the first to comment!")

        return render(request, 'posts/detail.html', {
            'post': post,
            'comments': comments,
        })

    except Exception as e:
        # Log the error (in a real app)
        messages.error(request, "An error occurred while retrieving the post. You have been redirected back to your previous page.")
        
        # Redirect to the previous page or to the user's post list if the referrer is not available
        previous_page = request.META.get('HTTP_REFERER', 'posts:index')
        return redirect(previous_page)

# Update an existing post
@login_required
def update(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id, user=request.user)

        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                messages.success(request, "Your post has been successfully updated.")
                return redirect('posts:detail', post_id=post.id)
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = PostForm(instance=post)

        return render(request, 'posts/form.html', {
            'form': form,
            'title': 'Edit Post',
            'post': post,
            'is_editing': True,
        })

    except Exception as e:
        # Log the error (in a real app)
        messages.error(request, "An error occurred while updating the post. You have been redirected back to your previous page.")
        previous_page = request.META.get('HTTP_REFERER', 'posts:index')
        return redirect(previous_page)

# Delete a post
@login_required
def delete(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id, user=request.user)

        if request.method == 'POST':
            post.delete()
            messages.success(request, "Your post has been successfully deleted.")
            return redirect('posts:index')
            
        return render(request, 'posts/confirm_delete.html', {'post': post})

    except Exception as e:
        # Log the error (in a real app)
        messages.error(request, "An error occurred while deleting the post. You have been redirected back to your previous page.")
        previous_page = request.META.get('HTTP_REFERER', 'posts:index')
        return redirect(previous_page)

# Create a new comment
@login_required
def create_comment(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)

        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                try:
                    comment = form.save(commit=False)
                    comment.post = post
                    comment.user = request.user
                    comment.pub_date = timezone.now()
                    comment.save()
                    messages.success(request, "Your comment has been successfully added.")
                    return redirect('posts:detail', post_id=post.id)
                except Exception as e:
                    # Log the error (in a real app)
                    messages.error(request, "An error occurred while adding your comment. Please try again.")
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = CommentForm()

        return render(request, 'posts/comment_form.html', {
            'form': form,
            'post': post,
            'title': 'Add Comment',
        })

    except Exception as e:
        # Log the error (in a real app)
        messages.error(request, "An error occurred while processing your request. You have been redirected back to your previous page.")
        previous_page = request.META.get('HTTP_REFERER', 'posts:index')
        return redirect(previous_page)

# Displaying a single comment
@login_required
def comment_detail(request, comment_id):
    try:
        comment = get_object_or_404(Comment, id=comment_id)

        context = {
            'title': 'Comment Details',
            'subtitle': f'Comment by {comment.user.username}',
            'comment': comment,
        }
        return render(request, 'posts/comment_detail.html', context)

    except Exception as e:
        # Log the error (in a real app)
        messages.error(request, "An error occurred while retrieving the comment. You have been redirected back to your previous page.")
        previous_page = request.META.get('HTTP_REFERER', 'posts:index')
        return redirect(previous_page)


# Update an existing comment
@login_required
def update_comment(request, comment_id):
    try:
        comment = get_object_or_404(Comment, id=comment_id)

        # Ensure the user is the owner of the comment
        if comment.user != request.user:
            messages.error(request, "You do not have permission to edit this comment.")
            return redirect('posts:detail', post_id=comment.post.id)

        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request, "Your comment has been successfully updated.")
                return redirect('posts:detail', post_id=comment.post.id)
            else:
                messages.error(request, "Please correct the errors below.")
        else:
            form = CommentForm(instance=comment)

        context = {
            'title': 'Edit Comment',
            'subtitle': 'Update your comment below:',
            'form': form,
            'post': comment.post
        }

        return render(request, 'posts/comment_form.html', context)

    except Exception as e:
        # Log the error (in a real app)
        messages.error(request, "An error occurred while updating the comment. You have been redirected back to your previous page.")
        previous_page = request.META.get('HTTP_REFERER', 'posts:index')
        return redirect(previous_page)

# Delete a comment
@login_required
def delete_comment(request, comment_id):
    # Fetch the comment object or return a 404 error if it does not exist
    comment = get_object_or_404(Comment, id=comment_id)

    # Check if the user has permission to delete the comment
    if request.user != comment.user and request.user != comment.post.user:
        messages.error(request, "You do not have permission to delete this comment.")
        return redirect('posts:detail', post_id=comment.post.id)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, "The comment has been successfully deleted.")
        return redirect('posts:detail', post_id=comment.post.id)

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
            messages.success(request, "The post has been successfully deleted.")
            return redirect('posts:index')
        elif comment_id:
            comment = get_object_or_404(Comment, id=comment_id)
            post_id = comment.post.id  # Get the post ID related to the comment
            comment.delete()
            messages.success(request, "The comment has been successfully deleted.")
            return redirect('posts:detail', post_id=post_id)

    # For GET requests or if IDs are missing, show the confirmation page
    post_id = request.GET.get('post_id')
    comment_id = request.GET.get('comment_id')

    context = {}
    if post_id:
        context['post'] = get_object_or_404(Post, id=post_id)
    elif comment_id:
        context['comment'] = get_object_or_404(Comment, id=comment_id)
        context['post_id'] = context['comment'].post.id  # Pass the post ID for cancellation

    return render(request, 'posts/confirm_delete.html', context)
