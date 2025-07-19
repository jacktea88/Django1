from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, )
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now=False, auto_now_add=True, )
    slug = models.SlugField(max_length=50, )
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-pub_date", ]

    def __str__(self):
        # pass
        return self.title
