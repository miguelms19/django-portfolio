from django.shortcuts import render

from .models import BlogConfig


def allblogs(request):
    blogs = BlogConfig.objects
    return render(request, 'blog/allblogs.html', {'blogs':blogs})
