from django.shortcuts import render
from .models import Post, Category


# Create your views here.


def Blog(request):

    posts = Post.objects.all()
    Categorys = Category.objects.all()

    return render(request, "blog/blog.html", {"posts": posts, "Categorys": Categorys})


def Category_list(request, category_id):

    posts = Post.objects.filter(Category=category_id)

    return render(request, "blog/category.html", {"posts": posts, "Categorys": posts})
