from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('heading_text', 'user', 'pub_date', 'is_approved')
    list_filter = ('pub_date', 'is_approved')
    search_fields = ('heading_text', 'message_text')
    actions = ['approve_posts']
    inlines = [CommentInline]

    def approve_posts(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f"{queryset.count()} posts approved successfully.")
    approve_posts.short_description = "Approve selected posts"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'comments_text', 'pub_date', 'is_approved')
    list_filter = ('pub_date', 'is_approved')
    search_fields = ('comments_text',)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
