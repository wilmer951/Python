from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):

    title_category = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.title_category


class Post(models.Model):

    title_post = models.CharField(max_length=50)
    contenet = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blogpp', null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return self.title_post
