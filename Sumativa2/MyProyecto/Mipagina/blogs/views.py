from django.shortcuts import render
from django.http import HttpResponse
from blogs.models import Post, Category

def home_page(request):
    posts = Post.objects.all()
    categories = Category.objects.all()

    context = {
        'post_list':posts,
        'categories':categories,
    }

    return render(request, 'blogs/home_page.html', context=context)