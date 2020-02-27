from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Posts(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    title = models.CharField(max_length=150)
    post = models.TextField()
    dateOfPost = models.DateTimeField(default=timezone.now)
    like = models.ManyToManyField(User, related_name="liked_user", blank=True)
    dislike = models.ManyToManyField(
        User, related_name="disliked_user", blank=True)
    report = models.ManyToManyField(
        User, related_name="reported_user", blank=True)
    post_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
