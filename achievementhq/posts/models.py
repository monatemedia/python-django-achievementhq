from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    heading_text = models.CharField(max_length=60)
    message_text = models.CharField(max_length=280)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading_text
