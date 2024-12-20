from django.db import models
from django.contrib.auth.models import User
from Posts.models import Post

# Create your models here.

# Class for creating comments underpost. Includes which post, author, their message, and time posted
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    message  = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # The amount of upvotes(likes) and downvotes(dislikes)on the comment
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_comments', blank=True)
    
    # Used for replies to comments
    comment_reply = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    
    # Shows which user commented on which post
    def __str__(self):
        return f'Comment by: {self.author.username} on post: {self.post.title}'
    
    # Used for the default ordering of the comments, based on recent comment
    class Meta:
        ordering = ['-timestamp']
        
        