from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    update_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
