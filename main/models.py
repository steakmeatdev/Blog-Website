from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):

    ## That on_delete = models.CASCADE just means that if the user is deleted, than the post is deleted

    ## We will include the user dircetly from the request
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description